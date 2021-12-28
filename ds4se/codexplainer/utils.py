# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/8.8_codexplainer.utils.ipynb (unless otherwise specified).

__all__ = ['logger', 'fhandler', 'formatter', 'get_tabulardata_distances_data', 'get_data_stats_dataframe',
           'clean_dict_dataset_nans', 'clean_dataset_nans', 'integrate_missing_error_dims']

# Cell

import pandas as pd
import numpy as np

from typing import Tuple, List, Optional, Dict, Set

# Cell
#Logging configuration

import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename='mylog.log', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

# Cell

def get_tabulardata_distances_data(data: List,
                                   div_nm: Optional[str]='JS-Divergence',
                                   dist_nm: Optional[str]='JS-Distance') -> Tuple:
    """
    Get the tabular data for error distances (JS distance & divergence)

    :param err_data: List containing data of multiple experiments
    :pram div_nm: Optional[str] indicating the name of the divergence metrics in the data
    :pram dist_nm: Optional[str] indicating the name of the distance metrics in the data

    :return: Tuple[pd.DataFrame, pd.Dataframe] containing distance and divergence tabular data
    """
    dists = []
    divs = []

    for experiment in data:
        record_dist = { }
        record_div = { }

        for dimension, measures in experiment.items():
            record_dist[dimension] = measures[dist_nm]
            record_div[dimension] = measures[div_nm]

        dists.append(record_dist)
        divs.append(record_div)


    dist_df = pd.DataFrame(dists)
    div_df = pd.DataFrame(divs)

    return dist_df, div_df

# Cell

def get_data_stats_dataframe(stats_data: List,
                             measures: Optional[List[str]]=['mean']) -> Dict:
    """
    Get a set of dataframes for the stats data gathered accross all experiments
    Available for metrics & error analysis

    :param stats_data: List containing experimets data with metrics stats.
    :param measures: List[str] containing all the measures to consider
                     - ['mean'] considered by default

    :return: Dictionary containing pd.DataFrames for all the specified measures
    """
    data = { }

    for measure in measures:
        data[measure] = []

    for experiment in stats_data:
        for m in range(len(measures)):
            record = { }
            measure = measures[m]

            record  = { metric: stats[measure]  for metric, stats in experiment.items() }

            data[measure].append(record)

    data_df = { measure: pd.DataFrame(m_data)  for measure, m_data in data.items() }
    return data_df

# Cell

def clean_dict_dataset_nans(data: Dict, measures: Optional[List[str]]=['mean']):
    """
    Replace Nan values by mean
    :param data: Dict containing all "raw" dataframes for corresponding measures

    :return: Dictionary containing dataframes for each measure
    """
    clean_dict = { }
    for measure in measures:
        clean_dict[measure] = data[measure].fillna(data[measure].mean())

    return clean_dict

# Cell

def clean_dataset_nans(data: pd.DataFrame):
    clean_df = data.fillna(data.mean())
    return clean_df

# Cell

def integrate_missing_error_dims(df: pd.DataFrame, dimensions: Set):
    """
    Integrate dimensions in order to standarize dimensions for comparisons

    :return: pd.DataFrame with the integrated dimensions
    """

    result_df = df.copy()
    present_dims = list(df.columns)

    for dim in dimensions:
        if dim not in present_dims:
            result_df[dim] = np.zeros(len(df))

    return result_df