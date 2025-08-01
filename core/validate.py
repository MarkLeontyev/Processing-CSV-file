SUPPORTED_OPERATORS = {'=', '<', '>'}
UNSUPPORTED_OPERATORS = {'>=', '<=', '!=', '=='}

def validate_filter_operation(condition_str: str) -> None:
    """
    Проверяет, что в условии нет неподдерживаемых операторов.
    """
    for op in UNSUPPORTED_OPERATORS:
        if op in condition_str:
            raise ValueError(
                f"Оператор '{op}' не поддерживается. "
                f"Поддерживаются только операторы: {', '.join(sorted(SUPPORTED_OPERATORS))}."
            )

    if not any(op in condition_str for op in SUPPORTED_OPERATORS):
        raise ValueError(
            f"В условии отсутствует поддерживаемый оператор. "
            f"Поддерживаются только операторы: {', '.join(sorted(SUPPORTED_OPERATORS))}."
        )
