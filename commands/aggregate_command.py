from commands.base_command import BaseCommand
from core.csv_handlers import read_csv
from tabulate import tabulate
from typing import List, Dict, Any
from numbers import Number

class AggregateCommand(BaseCommand):
    def __init__(self, column: str, operation: str):
        self.column = column
        self.operation = operation.lower() 
        self._validate_operation()

    def _validate_operation(self):
        """Валидация поддерживаемых операций"""
        valid_operations = {'min', 'max', 'avg'}
        if self.operation not in valid_operations:
            raise ValueError(f"Неподдерживаемая операция: {self.operation}. Допустимые: {', '.join(valid_operations)}")

    def _validate_values(self, values: List[Any]):
        """Валидация значений для агрегации"""
        if not values:
            raise ValueError("Нет данных для агрегации")
        
        if not all(isinstance(v, Number) for v in values):
            raise ValueError("Все значения должны быть числами")

    def execute(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        values = [row[self.column] for row in data if self.column in row]
        
        try:
            self._validate_values(values)
            
            if self.operation == 'min':
                result = min(values)
            elif self.operation == 'max':
                result = max(values)
            elif self.operation == 'avg':
                result = sum(values) / len(values)
            
            return [{'column': self.column, 'operation': self.operation, 'result': result}]
        
        except ValueError as e:
            return [{'error': str(e)}]