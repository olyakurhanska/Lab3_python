
"""Функції для обчислення результатів студентів."""

from ..models.grades import parse_grade


def average_grade(values: list[str]) -> float:
    """Обчислює середню оцінку студентів.

    Args:
        values (list[str]): Список оцінок у вигляді рядків.

    Returns:
        float: Середнє значення оцінок.

    Raises:
        ValueError: Якщо список порожній.
        ValidationError: Якщо оцінка не є числом.
        GradeLimitError: Якщо оцінка поза межами 0-100.
    """
    grades = [parse_grade(value) for value in values]

    if not grades:
        raise ValueError("Список оцінок порожній")

    return sum(grades) / len(grades)
