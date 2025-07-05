import pytest

from commands.filter_command import WhereCommand


def test_parse_condition_valid():
    cmd = WhereCommand("price>100")
    assert cmd.column == "price"
    assert cmd.operator == ">"
    assert cmd.value == 100

    cmd = WhereCommand("brand=apple")
    assert cmd.column == "brand"
    assert cmd.operator == "="
    assert cmd.value == "apple"

    cmd = WhereCommand('rating<4.5')
    assert cmd.column == "rating"
    assert cmd.operator == "<"
    assert cmd.value == 4.5

def test_parse_condition_invalid_operator():
    with pytest.raises(ValueError):
        WhereCommand("price!=100")

def test_convert_value_numeric_and_string():
    cmd = WhereCommand("price=123")
    assert isinstance(cmd.value, int)
    assert cmd.value == 123

    cmd = WhereCommand("rating=4.56")
    assert isinstance(cmd.value, float)
    assert cmd.value == 4.56

    cmd = WhereCommand('brand="apple"')
    assert isinstance(cmd.value, str)
    assert cmd.value == "apple"

    cmd = WhereCommand("brand='samsung'")
    assert isinstance(cmd.value, str)
    assert cmd.value == "samsung"

def test_execute_filter_numeric():
    data = [
        {"price": 50},
        {"price": 150},
        {"price": 100},
        {"price": "not_a_number"},
    ]
    cmd = WhereCommand("price>100")
    result = cmd.execute(data)
    assert len(result) == 1
    assert result[0]["price"] == 150

def test_execute_filter_string():
    data = [
        {"brand": "apple"},
        {"brand": "samsung"},
        {"brand": "xiaomi"},
    ]
    cmd = WhereCommand("brand=apple")
    result = cmd.execute(data)
    assert len(result) == 1
    assert result[0]["brand"] == "apple"

def test_execute_filter_missing_column():
    data = [
        {"price": 100},
        {"cost": 200},
    ]
    cmd = WhereCommand("price>50")
    result = cmd.execute(data)
    assert len(result) == 1
    assert result[0]["price"] == 100

def test_execute_filter_empty_data():
    cmd = WhereCommand("price>100")
    result = cmd.execute([])
    assert result == []

def test_execute_filter_type_mismatch():
    data = [
        {"price": "abc"},
        {"price": 150},
    ]
    cmd = WhereCommand("price>100")
    result = cmd.execute(data)
    assert len(result) == 1
    assert result[0]["price"] == 150