import csv
import re


def read_csv(filepath):
    """
    Читает CSV-файл и возвращает список словарей.
    """
    with open(filepath, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [convert_types(row) for row in reader]

def load_data(filename):
    """
    Загружает данные из CSV-файла и возвращает список словарей.
    """
    with open(filename) as f:
        reader = csv.DictReader(f)
        return [convert_types(row) for row in reader]

def convert_types(row):
    """
    Конвертирует значения словаря.
    """
    return {k: parse(v) for k, v in row.items()}

def parse(val: str):
    """
    Преобразует строковое значение.
    """
    val = val.strip()
    if val == "":
        return None
    if re.fullmatch(r'[+-]?\d+', val):
        return int(val)
    if re.fullmatch(r'[+-]?\d*\.\d+', val):
        return float(val)
    if re.fullmatch(r'[A-Za-z0-9]+', val):
        return val
    return val
