# AUTOGENERATED! DO NOT EDIT! File to edit: dev/2.3_repr.word2vec.train.ipynb (unless otherwise specified).

__all__ = ['LoadCorpus', 'SaveModel', 'LoadWord2Vec', 'LoadDoc2vec']

# Cell
# Imports
import numpy as np
import pandas as pd

from pathlib import Path
from datetime import datetime
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec, Doc2Vec

# Cell
#export
def LoadCorpus(params, sep=',', mode='a'):
    path_to_link = params['saving_path'] + '['+ params['system']  + '-' + params['version'] + '-{}].csv'.format(params['timestamp'])
    return pd.read_csv(path_to_link, header=0, index_col=0, sep=sep)

# Cell
def SaveModel(model, params, model_type='word2vec', description=''):
    timestamp = datetime.timestamp(datetime.now())
    path_to_link = params['saving_model'] + '['+ model_type  + '-' + description + '-{}].model'.format(timestamp)
    model.save(path_to_link)
    logging.info('Saving in...' + path_to_link)
    pass

# Cell
def LoadWord2Vec(timestamp, params, model_type='word2vec', description=''):
    path_to_link = params['saving_model'] + '['+ model_type + '-' + description + '-{}].model'.format(timestamp)
    return Word2Vec.load(path_to_link)

# Cell
def LoadDoc2vec(timestamp, params, model_type='doc2vec', description=''):
    path_to_link = params['saving_model'] + '['+ model_type + '-' + description + '-{}].model'.format(timestamp)
    return Doc2Vec.load(path_to_link)