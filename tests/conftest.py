from _pytest._py.path import LocalPath
import pytest
import json
import pandas as pd


@pytest.fixture(scope="session")
def tmpdir(tmpdir_factory) -> LocalPath:
    tmpdir = tmpdir_factory.mktemp("gimix")
    return tmpdir


@pytest.fixture(scope="session")
def text_file(tmpdir) -> str:
    text_file = str(tmpdir.join("test.txt"))
    with open(text_file, mode="w", encoding="utf-8") as file:
        file.write("abc")
    return text_file


@pytest.fixture(scope="session")
def json_file(tmpdir) -> str:
    json_file = str(tmpdir.join("test.json"))
    contents = {
        "key" : "value",
        "key_list" : [1, 2, 3],
        "key_dict" : {"a": 1, "b": 2, "c": "123"},
    }
    with open(json_file, mode="w", encoding="utf-8") as file:
        json.dump(contents, file)
    return json_file

@pytest.fixture(scope="session")
def csv_file(tmpdir) -> str:
    csv_file = str(tmpdir.join("text.csv"))
    data = {
        "A": [1, 2, 3],
        "B": ["a", "b", "c"],
    }
    df = pd.DataFrame(data=data)
    df.to_csv(csv_file, index=False)
    return csv_file
