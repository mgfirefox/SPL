def start():
    while True:
        try:
            a = float(input("Введите a: "))
            b = float(input("Введите b: "))
            print("Частное числа", a, 'на', b, "равно", a / b)
        except ValueError:
            print("Введите числа, состоящие из цифр 0-9, знаков -(минус) или .(точка)")
        except ZeroDivisionError:
            print("Деление на ноль не определено")
        finally:
            user_choice = input("Нажмите Enter для продолжения или введите q для выхода: ")
            if user_choice == 'q':
                break
