from typing import Any
from pathlib import Path
from gimix.files.load import (
    load_json,
    readlines,
)

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
