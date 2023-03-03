from gimix import files
from pandas import DataFrame


def test_load_text(text_file):
    contents = files.load(text_file)
    assert contents[0] == "abc"


def test_load_json(json_file):
    contents = files.load(json_file)
    assert contents.get("key") == "value"
    assert contents.get("key_list") == [1, 2, 3]
    assert contents.get("key_dict") == {"a": 1, "b": 2, "c": "123"}


def test_load_csv(csv_file):
    df = files.load(csv_file)
    assert isinstance(df, DataFrame)
    data = df.to_dict(orient="records")
    assert data[0] == {"A": 1, "B": "a"}
    assert data[1] == {"A": 2, "B": "b"}
    assert data[2] == {"A": 3, "B": "c"}
