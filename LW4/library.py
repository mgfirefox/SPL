class Library:
    DEPARTMENT_FILENAME = "departments.txt"
    __departments = []

    @staticmethod
    def start():
        Library.read()

        while True:
            try:
                user_choice = int(input('''   Отделы
1. Вывести отделы
2. Добавить отдел
3. Удалить отдел
4. Отредактировать отдел

   Книги
5. Вывести книги отдела
6. Добавить книги в отдел
7. Удалить книги отдела
8. Отредактировать книгу отдела

9. Записать информацию в файл
0. Выход
'''))
            except ValueError:
                print("Введите целое число от 0 до 9")
                continue

            if user_choice < 0 or user_choice > 9:
                print("Введите целое число от 0 до 9")
                continue

            if user_choice == 0:
                break
            elif user_choice == 1:
                Library.print_departments()
            elif user_choice == 2:
                Library.add_department()
            elif user_choice == 3:
                Library.remove_department()
            elif user_choice == 4:
                Library.edit_department()
            elif user_choice == 5:
                Library.print_books()
            elif user_choice == 6:
                Library.add_books()
            elif user_choice == 7:
                Library.remove_books()
            elif user_choice == 8:
                Library.edit_book()
            else:
                Library.write()

    @staticmethod
    def write():
        with open(Library.DEPARTMENT_FILENAME, 'w', encoding="utf-8") as file:
            for department in Library.__departments:
                books = department.get_books()
                file.write(department.get_name() + ";" + str(len(books)) + "\n")

                for book in books:
                    file.write(book.get_name() + ";" + book.get_author_initials() + "\n")

    @staticmethod
    def read():
        try:
            with open(Library.DEPARTMENT_FILENAME, encoding="utf-8") as file:
                while True:
                    line = file.readline()

                    if line == "":
                        break

                    department_data = line[:-1].split(";")
                    books = []

                    for i in range(int(department_data[1])):
                        books_data = file.readline()[:-1].split(";")
                        books.append(Book(books_data[0], books_data[1]))

                    Library.__departments.append(Department(department_data[0], books))
        except FileNotFoundError:
            pass

    @staticmethod
    def print_departments():
        if len(Library.__departments) == 0:
            print("Нет отделов")
            return

        for department in Library.__departments:
            print(department)

    @staticmethod
    def print_books():
        department_name = Department.input_name()

        for department in Library.__departments:
            if department.get_name() == department_name:
                department.print_books()
                break
        else:
            print("Нет такого отдела")

    @staticmethod
    def add_department():
        department = Department()
        department.input()
        Library.__departments.append(department)

    @staticmethod
    def add_books():
        department_name = Department.input_name()

        for department in Library.__departments:
            if department.get_name() == department_name:
                books = Department.input_books()
                department.add_books(books)
                break
        else:
            print("Нет такого отдела")

    @staticmethod
    def remove_department():
        name = Department.input_name()

        for department in Library.__departments:
            if department.get_name() == name:
                Library.__departments.remove(department)
                break
        else:
            print("Нет такого отдела")

    @staticmethod
    def remove_books():
        department_name = Department.input_name()

        for department in Library.__departments:
            if department.get_name() == department_name:
                books = Department.input_books()
                department.remove_books(books)
                break
        else:
            print("Нет такого отдела")

    @staticmethod
    def edit_department():
        name = Department.input_name()

        for department in Library.__departments:
            if department.get_name() == name:
                department.set_name(Department.input_name())
        else:
            print("Нет такого отдела")

    @staticmethod
    def edit_book():
        department_name = Department.input_name()

        for department in Library.__departments:
            if department.get_name() == department_name:
                book = Book()
                book.input()

                books = department.get_books()
                for book1 in books:
                    if str(book1) == str(book):
                        new_book_name = Book.input_name()
                        new_book_author_initials = Book.input_author_initials()

                        if new_book_name != "":
                            book1.set_name(new_book_name)
                        if new_book_author_initials != "":
                            book1.set_author_initials(new_book_author_initials)

                        break
                else:
                    print("Нет такой книги")

                department.set_books(books)
                break
        else:
            print("Нет такого отдела")


class Department:
    def __init__(self, name: str = None, books: list = None):
        self.__name = name or ""
        self.__books = books or []

    def __str__(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_books(self):
        return self.__books

    def set_name(self, name: str):
        self.__name = name

    def set_books(self, books: list):
        self.__books = books

    def input(self):
        self.__name = Department.input_name()
        self.__books = Department.input_books()

    @staticmethod
    def input_name():
        return input("Введите название отдела: ")

    @staticmethod
    def input_books():
        books = []

        print("Введите книги отдела")
        while True:
            book = Book()
            book.input()

            if book.get_name() == "" or book.get_author_initials() == "":
                break

            books.append(book)

        return books

    def add_books(self, books):
        for book in books:
            self.__books.append(book)

    def remove_books(self, books):
        for book in books:
            try:
                self.__books.remove(book)
            except ValueError:
                print("Нет такой книги")

    def print_books(self):
        if len(self.__books) == 0:
            print("Нет книг в отделе")
            return

        for book in self.__books:
            print(book)


class Book:
    def __init__(self, name: str = None, author_initials: str = None):
        self.__name = name or ""
        self.__author_initials = author_initials or ""

    def __str__(self):
        return f"{self.__name} {self.__author_initials}"

    def get_name(self):
        return self.__name

    def get_author_initials(self):
        return self.__author_initials

    def set_name(self, name: str):
        self.__name = name

    def set_author_initials(self, author_initials: str):
        self.__author_initials = author_initials

    def input(self):
        self.__name = Book.input_name()
        self.__author_initials = Book.input_author_initials()

    @staticmethod
    def input_name():
        return input("Введите название книги: ")

    @staticmethod
    def input_author_initials():
        return input("Введите инициалы автора: ")
