import task1
import task2
import task3
import task4

while True:
    try:
        user_choice = int(input("Введите номер задания (от 1 до 4) или 0 для выхода: "))
    except ValueError:
        print("Введите целое число от 0 до 4")
        continue

    if user_choice < 0 or user_choice > 4:
        print("Введите целое число от 0 до 4")
        continue

    if user_choice == 0:
        break
    elif user_choice == 1:
        task1.start()
    elif user_choice == 2:
        task2.start()
    elif user_choice == 3:
        task3.start()
    elif user_choice == 4:
        task4.start()
