import random


def start():
    numbers_tuple = tuple(random.randint(-1000000000, 1000000000) for _ in range(10))
    print(numbers_tuple)

    numbers_tuple = tuple(sorted(numbers_tuple, reverse=True))
    print("Кортеж отсортирован в порядке убывания:")
    print(numbers_tuple)

    print("Его первый элемент: ", numbers_tuple[0],
          ", последний — ", numbers_tuple[-1], sep='')
