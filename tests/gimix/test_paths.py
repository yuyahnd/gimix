import pytest
import os
from gimix import paths

@pytest.mark.parametrize("path, filename", [
    ("test.txt",       "test.txt"),
    ("./test.txt",     "test.txt"),
    ("./dir/test.txt", "test.txt"),
    ("test",           "test"),
    ("./test",         "test"),
])
def test_filename(path, filename):
    result = paths.filename(path)
    assert filename == result


@pytest.mark.parametrize("path, suffix", [
    ("test.txt",       ".txt"),
    ("./test.txt",     ".txt"),
    ("./dir/test.txt", ".txt"),
    ("test",           ""),
    ("./test",         ""),
])
def test_suffix(path, suffix):
    result = paths.suffix(path)
    assert suffix == result


@pytest.mark.parametrize("base, path", [
    ("base", ""),
    ("base", "/a"),
    ("base", ("a")),
    ("base", ("a", "b")),
    ("base", ("a", "/b")),
])
def test_join(base, path):
    result = paths.join(base, *path)
    assert result == os.path.join(base, *path).replace(os.path.sep, "/")
