from typing import Any, Dict, List, Optional

from tabulate import tabulate


def print_table(
    data: List[Dict[str, Any]],
    headers: Optional[str] = "keys",
    tablefmt: str = "fancy_grid"
) -> None:
    """
    Красиво выводит список словарей в консоль в виде таблицы.
    """
    if not data:
        print("Нет данных для отображения")
        return

    print(tabulate(data, headers=headers, tablefmt=tablefmt))
