import pytest

from commands.aggregate_command import AggregateCommand


def test_aggregate_min():
    data = [{'price': 10}, {'price': 5}, {'price': 20}]
    cmd = AggregateCommand('price', 'min')
    result = cmd.execute(data)
    assert result == [{'column': 'price', 'operation': 'min', 'result': 5}]

def test_aggregate_max():
    data = [{'price': 10}, {'price': 5}, {'price': 20}]
    cmd = AggregateCommand('price', 'max')
    result = cmd.execute(data)
    assert result == [{'column': 'price', 'operation': 'max', 'result': 20}]

def test_aggregate_avg():
    data = [{'rating': 4.5}, {'rating': 5.0}, {'rating': 4.0}]
    cmd = AggregateCommand('rating', 'avg')
    result = cmd.execute(data)
    expected_avg = (4.5 + 5.0 + 4.0) / 3
    assert result == [{'column': 'rating', 'operation': 'avg', 'result': expected_avg}]

def test_aggregate_empty_data():
    data = []
    cmd = AggregateCommand('price', 'min')
    result = cmd.execute(data)
    assert 'error' in result[0]
    assert result[0]['error'] == 'Нет данных для агрегации'

def test_aggregate_column_not_in_data():
    data = [{'price': 10}, {'cost': 5}]
    cmd = AggregateCommand('rating', 'max')
    result = cmd.execute(data)
    assert 'error' in result[0]
    assert result[0]['error'] == 'Нет данных для агрегации'

def test_aggregate_non_numeric_values():
    data = [{'price': 10}, {'price': 'abc'}, {'price': 20}]
    cmd = AggregateCommand('price', 'min')
    result = cmd.execute(data)
    assert 'error' in result[0]
    assert result[0]['error'] == 'Все значения должны быть числами'

def test_aggregate_invalid_operation():
    with pytest.raises(ValueError):
        AggregateCommand('price', 'sum')

def test_aggregate_case_insensitive_operation():
    data = [{'price': 10}, {'price': 20}]
    cmd = AggregateCommand('price', 'AVG')
    result = cmd.execute(data)
    expected_avg = (10 + 20) / 2
    assert result == [{'column': 'price', 'operation': 'avg', 'result': expected_avg}]
