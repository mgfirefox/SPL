import task2
import library


if __name__ == "__main__":
    while True:
        try:
            user_choice = int(input("Введите номер задания (от 2 до 3) или 0 для выхода: "))
        except ValueError:
            print("Введите целое число от 2 до 3 или 0")
            continue

        if user_choice == 0:
            break
        elif user_choice == 2:
            task2.start()
        elif user_choice == 3:
            library.Library.start()
        else:
            print("Введите целое число от 2 до 3 или 0")
