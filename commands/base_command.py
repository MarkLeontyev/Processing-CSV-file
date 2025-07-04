from abc import ABC, abstractmethod
from typing import List, Dict, Any, Union

class BaseCommand(ABC):
    @abstractmethod
    def execute(self, args: Any, rows: List[Dict[str, Any]]) -> Union[List[Dict[str, Any]], Any]:
        pass