# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/0.3_mgmnt.prep.bpe.ipynb (unless otherwise specified).

__all__ = ['jsonl_list_to_dataframe', 'get_dfs', 'df_to_txt_file', 'sp_model_from_df', 'sp_model_from_glob',
           'gen_hugface_model', 'tokenize_fns', 'read_bpe_files', 'split_lines_to_files', 'get_ground_truth',
           'get_non_ground_truth', 'gen_gt_ngt']

# Cell
# Imports
import pandas as pd
import random
import sentencepiece as sp

from fastprogress.fastprogress import master_bar
from pathlib import Path
from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing

# Cell
def jsonl_list_to_dataframe(file_list, columns=None):
    """Load a list of jsonl.gz files into a pandas DataFrame."""
    return pd.concat([pd.read_json(f,
                                   orient='records',
                                   compression='gzip',
                                   lines=True)[columns]
                      for f in file_list], sort=False)

# Cell
def get_dfs(path):
    """
        Grabs the different data splits and converts them into dataframes.
        Expects format from Code Search Net Challenge.
    """
    dfs = []
    for split in ["train", "valid", "test"]:
        files = sorted((path/split).glob("**/*.gz"))
        df = jsonl_list_to_dataframe(files, ["code", "docstring"])
        dfs.append(df)

    return dfs

# Cell
def df_to_txt_file(df, output, cols):
    """Converts a dataframe and converts it into a text file that SentencePiece can use to train a BPE model"""
    if cols is None: cols = list(df.columns)
    merged_df = pd.concat([df[col] for col in cols])

    with open(output/'text.txt', 'w') as f:
        f.write('\n'.join(list(merged_df)))
    return output/'text.txt'

# Cell
def sp_model_from_df(df, output, model_name, cols = None):
    """Trains a SentencePiece BPE model from a pandas dataframe"""
    fname = df_to_txt_file(df, output, cols)
    sp.SentencePieceTrainer.train(f'--input={fname} --model_prefix={output / model_name} --hard_vocab_limit=false')

# Cell
def sp_model_from_glob(path, glob, model_name):
    fns = list(path.glob(glob))
    fns = ",".join(map(str, fns))
    sp.SentencePieceTrainer.train(f'--input={fns} --model_prefix={path / model_name} --hard_vocab_limit=false')

# Cell
def gen_hugface_model(df, output, tokenizer = ByteLevelBPETokenizer(), vocab_sz = 30_000, min_freq = 3, cols = None):
    fname = df_to_txt_file(df, output, cols)
    tokenizer.train(files = [str(fname)], vocab_size = vocab_sz, min_frequency = min_freq, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])

    return tokenizer

# Cell
def tokenize_fns(fns, tokenizer, exts, output, data_type):
    docs = []
    for fn in fns:
        system = fn.parent.name
        output_path = output/system/data_type
        output_path.mkdir(parents=True, exist_ok=True)
        files = []
        for ext in exts:
            files.extend(fn.glob(f'**/*.{ext}'))
        for file in files:
            if 'README' not in file.name:
                with open(file, encoding='ISO-8859-1') as f:
                    docs.append(tokenizer.EncodeAsPieces(f.read()))
                with open((output_path/file.name).with_suffix('.bpe'), 'w') as f:
                    f.write(' '.join(docs[-1]))

    return docs

# Cell
def read_bpe_files(path):
    bpe_files = []
    for file in path.glob('**/*.bpe'):
        with open(file) as f:
            bpe_files.append(f.read().split(' '))

    return bpe_files

# Cell
def split_lines_to_files(lines, fn_pattern, output_path, tokenizer):
    for line in lines:
        fn, content = line.split(fn_pattern)
        fn = fn.replace('"', '')
        fn = fn.replace(' Test ', '')
        content = tokenizer.EncodeAsPieces(content)
        with open((output_path/fn).with_suffix('.bpe'), 'w') as f:
                    f.write(' '.join(content))

# Cell
def get_ground_truth(path, language):
    all_links = pd.DataFrame([], columns = [
        'sys', 'from_type', 'to_type', 'from_file', 'to_file', 'from_doc', 'to_doc'
    ])
    for fn in path.glob('*.txt'):
        content = str(fn.name).split('.')[0][1:-1]
        content = content.split('-')

        sys, from_type, to_type = content[0], content[2], content[4]

        with open(fn) as f:
            links = f.read().split('\n')[:-1]

        for link in links:
            link = link.split(' ')
            root, children = link[0], link[1:]
            root = Path(root).with_suffix('.bpe').name
            with open(path.parent.parent/'bpe'/language/sys/from_type/root) as f:
                root_content = f.read().split(' ')
            children = [Path(child).with_suffix('.bpe').name for child in children]
            children = [Path('.'.join(str(child).split('.')[-2:])) for child in children]
            for child in children:
                with open(path.parent.parent/'bpe'/language/sys/to_type/child) as f:
                    child_content = f.read().split(' ')
                all_links = all_links.append({'sys': sys,
                                              'from_type': from_type,
                                              'to_type': to_type,
                                              'from_file': root,
                                              'to_file': str(child),
                                              'from_doc': root_content,
                                              'to_doc': child_content},
                                             ignore_index=True)

    return all_links

# Cell
def get_non_ground_truth(path, language, gt):
    all_non_links = []

    existing_links = ['->'.join(link) for link in zip(gt['from_file'].to_list(), gt['to_file'].to_list())]
    bpe_files = list(path.glob('**/*.bpe'))
    random.shuffle(bpe_files)
    for i in bpe_files[:500]:
        sys = i.parent.parent.name
        from_type = i.parent.name
        if str(from_type) != 'req': continue
        with open(i) as f:
            i_content = f.read().split(' ')
        random.shuffle(bpe_files)
        for j in bpe_files[:500]:
            if i == j: continue
            if '->'.join([i.name, j.name]) in existing_links: continue
            to_type = j.parent.name
            if str(to_type) == 'req': continue
#             if from_type == to_type: continue
            with open(j) as f:
                j_content = f.read().split(' ')
            all_non_links.append([sys, from_type, to_type, i.name, j.name, i_content, j_content])

    all_non_links = pd.DataFrame(all_non_links, columns = [
        'sys', 'from_type', 'to_type', 'from_file', 'to_file', 'from_doc', 'to_doc'
    ])
    return all_non_links

# Cell
def gen_gt_ngt(path, lang):
    gt = get_ground_truth(path/'groundtruth'/lang, lang)
    ngt = get_non_ground_truth(path/'bpe'/lang, lang, gt)

    return gt, ngt