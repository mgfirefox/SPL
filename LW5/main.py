import task1
import task2
import task3


if __name__ == "__main__":
    while True:
        try:
            user_choice = float(input("Введите номер задания (1.1-1.2, 2, 3.1-3.2) или 0 для выхода: "))
        except ValueError:
            print("Введите число 1.1, 1.2, 2, 3.1, 3.2 или 0")
            continue

        if user_choice == 0:
            break
        elif user_choice == 1.1:
            task1.start1()
        elif user_choice == 1.2:
            task1.start2()
        elif user_choice == 2:
            task2.start()
        elif user_choice == 3.1:
            task3.start1()
        elif user_choice == 3.2:
            task3.start2()
