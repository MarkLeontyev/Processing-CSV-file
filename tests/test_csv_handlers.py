import os
import tempfile

import pytest

from core.csv_handlers import convert_types, load_data, parse, read_csv

@pytest.mark.parametrize("input_str, expected", [
    ("123", 123),
    ("-45", -45),
    ("+78", 78),
    ("3.14", 3.14),
    ("-0.99", -0.99),
    ("apple123", "apple123"),
    ("X123", "X123"),
    ("", None),
    ("   ", None),
    ("abcDEF", "abcDEF"),
    ("12a34", "12a34"),
    ("hello_world", "hello_world"),
    ("12 34", "12 34"),
])
def test_parse(input_str, expected):
    assert parse(input_str) == expected

def test_convert_types():
    row = {
        "int": "123",
        "float": "45.6",
        "str": "hello123",
        "empty": "",
        "mixed": "abc123",
        "underscore": "hello_world",
        "space": "hello world",
    }
    converted = convert_types(row)
    assert converted["int"] == 123
    assert converted["float"] == 45.6
    assert converted["str"] == "hello123"
    assert converted["empty"] is None
    assert converted["mixed"] == "abc123"
    assert converted["underscore"] == "hello_world"
    assert converted["space"] == "hello world"

def create_temp_csv(content: str):
    tmp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', newline='')
    tmp_file.write(content)
    tmp_file.close()
    return tmp_file.name

@pytest.mark.parametrize("func", [read_csv, load_data])
def test_read_load_data(func):
    csv_content = """name,age,salary
Mark,30,1000
Alina,25,2000
Ilya,,1500
"""
    tmp_path = create_temp_csv(csv_content)
    try:
        data = func(tmp_path)
        assert isinstance(data, list)
        assert len(data) == 3
        assert data[0]["name"] == "Mark"
        assert data[0]["age"] == 30
        assert data[0]["salary"] == 1000
        assert data[2]["age"] is None
    finally:
        os.unlink(tmp_path)
