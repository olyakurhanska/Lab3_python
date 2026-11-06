
from pathlib import Path


def check_grade(value):
    print("\nСценарій 1: try/except")
    try:
        grade = int(value)
        print(f"Успіх: оцінка {grade}")
    except ValueError:
        print("Помилка ValueError: оцінка має бути числом")


def calculate_average(grades):
    print("\nСценарій 2: try/except/else/finally")
    try:
        average = sum(grades) / len(grades)
    except ZeroDivisionError:
        print("Помилка ZeroDivisionError: список оцінок порожній")
    else:
        print(f"Успіх: середня оцінка {average:.2f}")
    finally:
        print("Обчислення завершено")


def find_student(students, index):
    print("\nСценарій 3: кілька типів виключень")
    try:
        student = students[int(index)]
        print(f"Успіх: знайдено студента {student}")
    except (ValueError, IndexError) as error:
        print(f"Помилка {type(error).__name__}: {error}")


def read_students(filename):
    print("\nСценарій 4: робота з файлом через with")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read().strip())
    except FileNotFoundError:
        print("Помилка FileNotFoundError: файл не знайдено")


def main():
    check_grade("85")
    check_grade("abc")

    calculate_average([85, 92, 78])
    calculate_average([])

    students = ["Олена", "Іван", "Марія"]
    find_student(students, "1")
    find_student(students, "10")
    find_student(students, "abc")

    Path("students.txt").write_text(
        "Олена: 95\nІван: 78\nМарія: 92",
        encoding="utf-8"
    )

    read_students("students.txt")
    read_students("missing.txt")


if __name__ == "__main__":
    main()
