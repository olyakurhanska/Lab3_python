
"""Власні виключення для роботи з даними студентів."""


class StudentAppError(Exception):
    """Базове виключення програми."""
    pass


class ValidationError(StudentAppError):
    """Помилка перетворення або перевірки даних."""

    def __init__(self, field: str, value: str):
        """Зберігає назву поля та некоректне значення."""
        self.field = field
        self.value = value

    def __str__(self) -> str:
        """Повертає текст повідомлення про помилку."""
        return f"Некоректне значення поля {self.field}: {self.value}"


class StudentNotFoundError(StudentAppError):
    """Помилка пошуку студента за ідентифікатором."""

    def __init__(self, student_id: int):
        """Зберігає ідентифікатор відсутнього студента."""
        self.student_id = student_id

    def __str__(self) -> str:
        """Повертає повідомлення про відсутнього студента."""
        return f"Студента з ID {self.student_id} не знайдено"


class GradeLimitError(StudentAppError):
    """Помилка оцінки за межами допустимого діапазону."""

    def __init__(self, grade: int):
        """Зберігає недопустиму оцінку."""
        self.grade = grade

    def __str__(self) -> str:
        """Повертає повідомлення про недопустиму оцінку."""
        return f"Оцінка {self.grade} виходить за межі 0-100"
