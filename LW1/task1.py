import random


def start():
    number = random.randint(1, 1000000000)
    print("Число:", number)

    odd_digits_sum = 0

    for digit in str(number):
        if int(digit) % 2 == 1:
            odd_digits_sum += int(digit)

    print("Сумма нечетных цифр числа равна", odd_digits_sum)
