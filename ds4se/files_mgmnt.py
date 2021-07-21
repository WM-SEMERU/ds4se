# AUTOGENERATED! DO NOT EDIT! File to edit: dev/0.13_files_mgmnt.ipynb (unless otherwise specified).

__all__ = ['get_files_list', 'jsonl_list_to_dataframe', 'jsonl_to_dataframe', 'csv_to_dataframe']

# Cell

import pandas as pd

from pathlib import Path
from typing import List

# Cell

def _check_file_existence(file_path: str) -> bool:
    """
    Validates the existence of a file
    """
    path = Path(file_path)
    if not path.exists():
        logging.error('Provided file cannot be found.')
        return False
    return True

# Cell

def get_files_list(directory: str, file_extension: str) -> List[str]:
    """
    Get a list of files (with a specific extension) within a directory.
    :param directory: Directory to extract list of files
    :param file_extension: File extension of files to include in the list

    :return: List of files within the directoy with the provided extension
    """
    path = Path(directory)

    return list(path.glob(f'**/*.{file_extension}'))

# Cell

def jsonl_list_to_dataframe(file_list: List[str]) -> pd.DataFrame:
    """Load a list of jsonl.gz files into a pandas DataFrame."""
    return pd.concat([pd.read_json(f,
                                   orient='records',
                                   compression='gzip',
                                   lines=True)
                      for f in file_list], sort=False)

def jsonl_to_dataframe(file_path: str) -> pd.DataFrame:
    """
    Gets a DataFrame from a jsonl file
    :param file_path: Location of the jsonl file
    :return:
    """

    _check_file_existence(file_path)
    return pd.read_json(file_path, orient='records', lines=True)

# Cell

def csv_to_dataframe(file_path: str) -> pd.DataFrame:
    """Gets a DataFrame from a csv file"""

    _check_file_existence(file_path)
    return pd.read_csv(file_path)