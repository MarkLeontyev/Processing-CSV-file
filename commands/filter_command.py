from commands.base_command import BaseCommand
from core.validate import SUPPORTED_OPERATORS, validate_filter_operation


class WhereCommand(BaseCommand):
    def __init__(self, condition_str):
        """
        Инициализирует команду фильтрации.
        """
        self.column, self.operator, self.value = self._parse_condition(condition_str)
        
    def _parse_condition(self, condition_str: str):
        """
        Разбирает строку.
        """
        validate_filter_operation(condition_str)
        operators = SUPPORTED_OPERATORS
        for op in operators:
            if op in condition_str:
                column, value = condition_str.split(op, 1)
                return column.strip(), op, self._convert_value(value.strip())
        raise ValueError(f"Некорректное условие: '{condition_str}'")
    
    def _convert_value(self, value_str):
        """
        Преобразует строку значения в число.
        Если неудачно, то возвращает строку без кавычек.
        """
        try:
            return float(value_str) if '.' in value_str else int(value_str)
        except ValueError:
            return value_str.strip('"\'')

    def execute(self, data):
        """
        Выполняет фильтрацию списка словарей по условию.
        """
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
