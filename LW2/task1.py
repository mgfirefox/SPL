def start():
    print("Проверка надежности пароля")
    password = input("Введите пароль: ")

    if is_password_good(password):
        print("Пароль надежный")
    else:
        print("Пароль не надежный")


def is_password_good(password):
    if len(password) < 10:
        return False

    is_lower_present = False
    is_upper_present = False

    for i in range(len(password)):
        if password[i].islower():
            is_lower_present = True

            if is_upper_present:
                return True
        elif password[i].isupper():
            is_upper_present = True

            if is_lower_present:
                return True

    return False
