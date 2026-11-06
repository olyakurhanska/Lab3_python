
from pathlib import Path

import student_app
import student_app.utils.files as files
from student_app.models.errors import GradeLimitError
from student_app import *
from student_app.utils.reports import average_grade


def main():
    print("Завдання 3. Організація модулів і пакетів")

    print("\nПеревірка оцінки:")
    print("Оцінка:", check_grade(95))

    print("\nОбчислення середньої оцінки:")
    result = average_grade(["85", "92", "78"])
    print(f"Середня оцінка: {result:.2f}")

    print("\nПеревірка власного виключення:")
    try:
        check_grade(120)
    except GradeLimitError as error:
        print("Помилка:", error)

    print("\nРобота з файлом:")
    Path("students_lab3.txt").write_text(
        "Олена: 95\nІван: 78\nМарія: 92",
        encoding="utf-8"
    )
    print(files.read_students("students_lab3.txt"))

    print("Перевірка __all__:")
    print("Дозволені імена:", student_app.__all__)
    print("StudentAppError:", StudentAppError.__name__)
    print("parse_grade імпортовано через *:",
          "parse_grade" in globals())


if __name__ == "__main__":
    main()
