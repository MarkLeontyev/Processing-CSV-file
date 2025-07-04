from typing import List, Dict, Any, Optional
from tabulate import tabulate

def print_table(
    data: List[Dict[str, Any]],
    headers: Optional[str] = "keys",
    tablefmt: str = "fancy_grid"
) -> None:
    """
    Красиво выводит список словарей в консоль в виде таблицы.

    :param data: список словарей с данными
    :param headers: заголовки таблицы, по умолчанию ключи словарей
    :param tablefmt: стиль оформления таблицы
    """
    if not data:
        print("Нет данных для отображения")
        return

    print(tabulate(data, headers=headers, tablefmt=tablefmt))
