from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union


class BaseCommand(ABC):
    """
    Абстрактный базовый класс. Метод execute() обязателен для реализации в наследниках.
    """
    @abstractmethod
    def execute(self, args: Any, rows: List[Dict[str, Any]]) -> Union[List[Dict[str, Any]], Any]:
        pass
