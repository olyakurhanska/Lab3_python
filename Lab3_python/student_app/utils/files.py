
"""Функції для читання файлів із даними студентів."""


def read_students(filename: str) -> str:
    """Зчитує текст із файлу.

    Args:
        filename (str): Назва або шлях до файлу.

    Returns:
        str: Вміст файлу.

    Raises:
        FileNotFoundError: Якщо файл не знайдено.
        OSError: Якщо файл неможливо прочитати.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
