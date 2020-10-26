# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/1.0_exp.i.ipynb (unless otherwise specified).

__all__ = ['df_to_txt_file', 'gen_sp_model', 'encode_text', 'dit_shannon', 'entropies_of_df_entries']

# Cell
def df_to_txt_file(df, output, cols):
    """Converts a dataframe into a text file that SentencePiece can use to train a BPE model"""
    if cols is None: cols = list(df.columns)
    merged_df = pd.concat([df[col] for col in cols])

    with open(output + '_text.txt', 'w') as f:
        f.write('\n'.join(list(merged_df)))
    return output + '_text.txt'

# Cell
def gen_sp_model(df, output, model_name, cols=None):
    """Trains a SentencePiece BPE model from a pandas dataframe"""
    fname = df_to_txt_file(df, output, cols)
    sp.SentencePieceTrainer.train(f'--input={fname} --model_prefix={output + model_name} --hard_vocab_limit=false --model_type=bpe')
    return output + model_name

# Cell
def encode_text(text, model_prefix):
    '''Encodes text using a pre-trained sp model, returns the occurrences of each token in the text'''
    sp_processor = sp.SentencePieceProcessor()
    sp_processor.Load(f"{model_prefix}.model")
    token_counts = Counter()
    encoding = sp_processor.encode_as_pieces(text)
    for piece in encoding:
        token_counts[piece] += 1
    return token_counts

# Cell
#Notes: token_counts is a counter object.
def dit_shannon(token_counts):
    '''Takes in a counter object of token occurrences, computes the entropy of the corpus that produced it'''
    num_tokens = 0
    for token in token_counts:
        num_tokens += token_counts[token]
    outcomes = list(set(token_counts.elements()))
    frequencies = []
    for token in token_counts:
        frequencies.append((token_counts[token])/num_tokens)
    d = dit.ScalarDistribution(outcomes, frequencies)
    return dit.shannon.entropy(d)

# Cell
def entropies_of_df_entries(df, col, model_prefix):
    '''Returns a list of the entropies of each entry in a dataframe column'''
    entropies = []
    for data in df[col]:
        token_counts= encode_text(data, model_prefix)
        entropies.append(dit_shannon(token_counts))
    return entropies