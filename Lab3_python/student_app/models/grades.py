
"""Перевірка та перетворення оцінок студентів."""

from .errors import ValidationError, GradeLimitError


def parse_grade(value: str) -> int:
    """Перетворює рядок на оцінку та перевіряє її.

    Args:
        value (str): Оцінка у вигляді рядка.

    Returns:
        int: Перевірена оцінка.

    Raises:
        ValidationError: Якщо значення не є числом.
        GradeLimitError: Якщо оцінка поза межами 0-100.
    """
    try:
        grade = int(value)
    except ValueError as error:
        raise ValidationError("grade", value) from error

    return check_grade(grade)


def check_grade(grade: int) -> int:
    """Перевіряє допустимість оцінки.

    Args:
        grade (int): Оцінка студента.

    Returns:
        int: Оцінка від 0 до 100.

    Raises:
        GradeLimitError: Якщо оцінка поза межами 0-100.
    """
    if grade < 0 or grade > 100:
        raise GradeLimitError(grade)
    return grade
