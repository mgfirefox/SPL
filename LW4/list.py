class List:
    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(self.__list)

    def __len__(self) -> int:
        return len(self.__list)

    def __getitem__(self, index):
        return self.__list[index]

    def __setitem__(self, index, element):
        self.__list[index] = element

    def __delitem__(self, index):
        del self.__list[index]

    def __add__(self, x):
        return self.__list + x

    def __iadd__(self, x):
        self.__list += x

        return self

    def copy(self):
        return self.__list.copy()

    def append(self, element):
        self.__list.append(element)

    def pop(self, index):
        return self.__list.pop(index)

    def count(self, element):
        return self.__list.count(element)

    def insert(self, index, element):
        return self.__list.insert(index, element)

    def remove(self, element):
        return self.__list.remove(element)
