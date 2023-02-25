from gimix import files

def test_load_text(text_file):
    contents = files.load(text_file)
    assert contents[0] == "abc"


def test_load_json(json_file):
    contents = files.load(json_file)
    assert contents.get("key") == "value"
    assert contents.get("key_list") == [1, 2, 3]
    assert contents.get("key_dict") == {"a": 1, "b": 2, "c": "123"}
