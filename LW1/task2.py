def start():
    while True:
        string = input("Введите строку, состоящую из a-z, A-Z: ")
        if string.isalpha():
            break

    upper_pair_amount = 0
    lower_pair_amount = 0

    for i in range(len(string) - 1):
        if string[i].isupper() == string[i + 1].isupper():
            if string[i].isupper():
                upper_pair_amount += 1
            else:
                lower_pair_amount += 1

    print("Количество пар верхнего регистра:", upper_pair_amount)
    print("Количество пар нижнего регистра:", lower_pair_amount)
