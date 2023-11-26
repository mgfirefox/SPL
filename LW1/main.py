import task1
import task2
import task3
import task4
import task5
import task6


if __name__ == "__main__":
    while True:
        try:
            user_choice = int(input("Введите номер задания (от 1 до 6) или 0 для выхода: "))
        except ValueError:
            print("Введите целое число от 0 до 6")
            continue

        if user_choice < 0 or user_choice > 6:
            print("Введите целое число от 0 до 6")
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
        elif user_choice == 5:
            task5.start()
        elif user_choice == 6:
            task6.start()
