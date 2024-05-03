from pathlib import Path


def filename(path: str) -> str:
    """Returns file name from path.

    Parameters
    ----------
    path : str
        path

    Returns
    -------
    str
        file name
    """
    return Path(path).name


def suffix(path: str) -> str:
    """Returns the file extension from a path.

    Parameters
    ----------
    path : str
        path

    Returns
    -------
    str
        extension
    """
    return Path(path).suffix


def join(base: str, *args: str) -> str:
    """Concatenates the specified path.

    Parameters
    ----------
    base : str
        base path

    Returns
    -------
    str
        specified path
    """
    return Path(base).joinpath(*args).as_posix()
