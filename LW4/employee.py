class Employee:
    def __init__(self, id: int = 0, full_name: str = ""):
        self._id = id
        self._full_name = full_name

    def __str__(self):
        return f"{self._id} {self._full_name}"

    def get_id(self):
        return self._id

    def get_full_name(self):
        return self._full_name

    def set_id(self, id: int):
        self._id = id

    def set_full_name(self, full_name: str):
        self._full_name = full_name

    def input(self):
        self._id = Employee.input_id()
        self._full_name = Employee.input_full_name()

    @classmethod
    def create(cls):
        employee = cls()
        employee.input()

        return employee

    @staticmethod
    def input_id():
        while True:
            try:
                id = int(input("Введите ID работника: "))

                if id <= 0:
                    print("ID работника должно быть положительным числом")
                    continue

                break
            except ValueError:
                print("ID работника должно быть числом")

        return id

    @staticmethod
    def input_full_name():
        return input("Введите ФИО работника: ")
