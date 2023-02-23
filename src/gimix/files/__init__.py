from typing import Any
from pathlib import Path
import json


def load(filename: str, mode: str="r", encoding: str="utf-8") -> Any:
    """Reads and returns the file contents according to the file extension.

    Parameters
    ----------
    filename : str
        file name
    mode : str, optional
        file open mode, by default "r"
    encoding : str, optional
        file encoding, by default UTF_8

    Returns
    -------
    Any
        file contents
    """
    pfile = Path(filename)
    suffix = pfile.suffix
    if suffix == ".json":
        contents = load_json(filename, mode=mode, encoding=encoding)
    else:
        contents = readlines(filename, mode=mode, encoding=encoding)
    return contents


def load_json(filename: str, mode: str="r", encoding: str="utf-8") -> dict:
    """Reads the contents of a json file and returns it as a dict.

    Parameters
    ----------
    filename : str
        file name
    mode : str, optional
        file open mode, by default "r"
    encoding : str, optional
        file encoding, by default UTF_8

    Returns
    -------
    dict
        json dict
    """
    with open(filename, mode=mode, encoding=encoding) as file:
        return json.load(file)


def readlines(filename: str, mode: str="r", encoding: str="utf-8") -> list:
    """Reads the contents of a text file and returns it as a list.

    Parameters
    ----------
    filename : str
        file name
    mode : str, optional
        file open mode, by default "r"
    encoding : str, optional
        file encoding, by default UTF_8

    Returns
    -------
    list
        text list
    """
    with open(filename, mode=mode, encoding=encoding) as file:
        return file.readlines()
