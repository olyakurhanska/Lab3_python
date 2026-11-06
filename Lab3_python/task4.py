
from student_app.models.grades import parse_grade, check_grade
from student_app.models.errors import GradeLimitError
from student_app.utils.files import read_students
from student_app.utils.reports import average_grade
import inspect


def main():
    print("Документація функції parse_grade:")
    print(inspect.getdoc(parse_grade))

    print("\nДокументація функції check_grade:")
    print(inspect.getdoc(check_grade))

    print("\nДокументація функції read_students:")
    print(inspect.getdoc(read_students))

    print("\nДокументація функції average_grade:")
    print(inspect.getdoc(average_grade))

    print("\nДокументація класу GradeLimitError:")
    print(inspect.getdoc(GradeLimitError))

    print("\nАнотації типів:")
    print("parse_grade:", parse_grade.__annotations__)
    print("average_grade:", average_grade.__annotations__)

    
    print("\nПеревірка help():")
    import pydoc
    print(pydoc.render_doc(check_grade, renderer=pydoc.plaintext))



if __name__ == "__main__":
    main()
