
class StudentAppError(Exception):
    pass


class ValidationError(StudentAppError):
    def __init__(self, field, value):
        self.field = field
        self.value = value

    def __str__(self):
        return f"Некоректне значення поля {self.field}: {self.value}"


class StudentNotFoundError(StudentAppError):
    def __init__(self, student_id):
        self.student_id = student_id

    def __str__(self):
        return f"Студента з ID {self.student_id} не знайдено"


class GradeLimitError(StudentAppError):
    def __init__(self, grade):
        self.grade = grade

    def __str__(self):
        return f"Оцінка {self.grade} виходить за межі 0-100"


def parse_grade(value):
    try:
        return int(value)
    except ValueError as error:
        raise ValidationError("grade", value) from error


def find_student(students, student_id):
    if student_id not in students:
        raise StudentNotFoundError(student_id)
    return students[student_id]


def check_grade(grade):
    if grade < 0 or grade > 100:
        raise GradeLimitError(grade)
    return grade


def process_grade(grade):
    try:
        return check_grade(grade)
    except GradeLimitError as error:
        print(f"Запис у журнал: {error}")
        raise


def main():
    students = {
        1: "Олена",
        2: "Іван",
        3: "Марія"
    }

    print("Сценарій 1: успішна обробка")
    print("Оцінка:", parse_grade("85"))
    print("Студент:", find_student(students, 2))

    print("\nСценарій 2: помилка валідації")
    try:
        parse_grade("abc")
    except ValidationError as error:
        print("Помилка:", error)
        print("Початкова причина:", type(error.__cause__).__name__)

    print("\nСценарій 3: студент не знайдений")
    try:
        find_student(students, 10)
    except StudentNotFoundError as error:
        print("Помилка:", error)

    print("\nСценарій 4: перевищення допустимої оцінки")
    try:
        check_grade(120)
    except GradeLimitError as error:
        print("Помилка:", error)

    print("\nСценарій 5: повторне піднесення виключення")
    try:
        process_grade(-5)
    except StudentAppError as error:
        print("Перехоплено через базовий клас:", error)


if __name__ == "__main__":
    main()
