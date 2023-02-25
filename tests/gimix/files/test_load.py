from gimix.files.load import (
    load_json,
    readlines,
)


def test_load_text(text_file):
    contents = readlines(text_file)
    assert contents[0] == "abc"


def test_load_json(json_file):
    contents = load_json(json_file)
    assert contents.get("key") == "value"
    assert contents.get("key_list") == [1, 2, 3]
    assert contents.get("key_dict") == {"a": 1, "b": 2, "c": "123"}
