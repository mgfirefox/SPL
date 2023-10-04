import random


def start():
    while True:
        try:
            user_choice = int(input('''Что хотите передать в функцию:
1. Кортеж строк
2. Список чисел
3. Число
4. Строка
0. Выход
'''))
        except ValueError:
            print("Введите целое число от 0 до 4")
            continue

        if user_choice < 0 or user_choice > 4:
            print("Введите целое число от 0 до 4")
            continue

        if user_choice == 0:
            break
        elif user_choice == 1:
            element = ("alter", "digit", "current", "vowel", "consonant", "fridge")
        elif user_choice == 2:
            element = [random.randint(-1000000000, 1000000000) for _ in range(10)]
        elif user_choice == 3:
            element = random.randint(0, 1000000000)
        else:
            element = "afj4848nje38f8uc4j4if88d3j4nf88r4"

        func(element)
        break


def func(element):
    if isinstance(element, tuple):
        print(element)

        for i in range(len(element)):
            if isinstance(element[i], str):
                for word in element[i].split():
                    print("Длина слова", word, "равна", len(word))
    elif isinstance(element, list):
        print(element)
        numbers_sum = 0

        for i in range(len(element)):
            if element[i] < 0:
                for j in range(i, len(element)):
                    if isinstance(element[i], int):
                        numbers_sum += element[j]
                else:
                    break

        print("Сумма чисел после отрицательного равна:", numbers_sum)

        for i in range(len(element) - 1):
            j = i + 1
            while j < len(element):
                if element[i] == element[j]:
                    del element[j]
                else:
                    j += 1
        print("Повторяющееся числа удалены:")
        print(element)
    elif isinstance(element, int):
        print("Число:", element)
        even_digits_amount = 0

        for digit in str(element):
            if int(digit) % 2 == 0:
                even_digits_amount += 1

        print("Количество четных цифр числа равна", even_digits_amount)
    elif isinstance(element, str):
        print("Строка:", element)
        numbers_sum = 0

        i = 0
        while i < len(element):
            if element[i].isdigit():
                for j in range(i + 1, len(element)):
                    if not element[j].isdigit():
                        numbers_sum += int(element[i:j])
                        i = j + 1
                        break
            i += 1

        print("Сумма чисел в строке равна", numbers_sum)
