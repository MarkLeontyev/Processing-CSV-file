import csv
import ast
from datetime import datetime

def read_csv(filepath):
    with open(filepath, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [convert_types(row) for row in reader]

def load_data(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return [convert_types(row) for row in reader]

def convert_types(row):
    return {k: try_eval(v) for k, v in row.items()}

def try_eval(val):
    val = val.strip()
    if val == "":
        return None
    try:
        return ast.literal_eval(val)
    except (ValueError, SyntaxError):
        return val
