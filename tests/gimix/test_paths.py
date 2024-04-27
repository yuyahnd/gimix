import pytest
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
