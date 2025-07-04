from core.csv_handlers import read_csv
from tabulate import tabulate

from commands.base_command import BaseCommand

class WhereCommand(BaseCommand):
    def __init__(self, condition_str):
        self.column, self.operator, self.value = self._parse_condition(condition_str)
        
    def _parse_condition(self, condition_str):
        """Разбирает условие на колонку, оператор и значение"""
        operators = ['=', '>', '<']
        for op in operators:
            if op in condition_str:
                column, value = condition_str.split(op, 1)
                return column.strip(), op, self._convert_value(value.strip())
        raise ValueError(f"Недопустимый оператор в условии: '{condition_str}'")

    def _convert_value(self, value_str):
        """Конвертирует строку значения в число, если возможно"""
        try:
            return float(value_str) if '.' in value_str else int(value_str)
        except ValueError:
            return value_str.strip('"\'')

    def execute(self, data):
        if not data:
            return []
            
        results = []
        for row in data:
            try:
                cell_value = row.get(self.column)
                if cell_value is None:
                    continue
                if self.operator == '>' and cell_value > self.value:
                    results.append(row)
                elif self.operator == '<' and cell_value < self.value:
                    results.append(row)
                elif self.operator == '=' and cell_value == self.value:
                    results.append(row)
            except (TypeError, ValueError):
                continue     
        return results