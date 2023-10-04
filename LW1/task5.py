def start():
    items_list = {"Торт": ["Описание1", 5, 2000],
                  "Пирожное": ["Описание2", 2.5, 3000],
                  "Маффин": ["Описание3", 2, 4500],
                  "Пончики": ["Описание4", 2, 2500]}

    while True:
        try:
            user_choice = int(input('''Добро пожаловать в программу "Кондитерская"
1. Просмотр описания продукции
2. Просмотр цены продукции
3. Просмотр количества продукции
4. Просмотр всей информации продукции
5. Покупка продукции
0. До свидания
Пожалуйста, введите номер пункта: '''))
        except ValueError:
            print("Введите целое число от 0 до 5")
            continue

        if user_choice < 0 or user_choice > 5:
            continue

        if user_choice == 0:
            break
        elif user_choice == 1:
            print("Название — Описание")
            for key in items_list:
                print(key, "—", items_list[key][0])
        elif user_choice == 2:
            print("Название — Цена (руб/100г)")
            for key in items_list:
                print(key, "—", items_list[key][1])
        elif user_choice == 3:
            print("Название — Количество (г)")
            for key in items_list:
                print(key, "—", items_list[key][2])
        elif user_choice == 4:
            print_all_information(items_list)
        elif user_choice == 5:
            order_list = {}

            while True:
                if not make_order(items_list, order_list):
                    break

            order_cost = 0

            print("Ваш заказ:")
            for key in order_list:
                cost = order_list[key] * items_list[key][1]
                order_cost += cost

                print(key, ' ', order_list[key], 'г ', cost, "руб", sep='')
            print("Итого: ", order_cost, "руб", sep='')

            print()
            print_all_information(items_list)


def print_all_information(items_list):
    print("Название — Описание — Цена (руб/100г) — Количество (г)")
    for key in items_list:
        print(key, "—", items_list[key][0], "—", items_list[key][1], "—", items_list[key][2])


def make_order(items_list, order_list):
    name = ''
    is_exist = False

    while not is_exist:
        name = input("Введите название продукции: ")
        if name == 'n':
            return False

        name = name.title()

        for key in items_list:
            if name == key:
                is_exist = True
                break
        else:
            print("Нет продукции с названием", name)

    while True:
        amount = input("Введите количество продукции: ")
        if amount == 'n':
            return False

        try:
            amount = int(amount)
        except ValueError:
            print("Число должно состоять из цифр 0—9")
            continue

        if amount <= 0:
            print("Число должно быть натуральным числом")
            continue
        if amount > items_list[name][2]:
            print("В наличии только ", items_list[name][2], "г продукции ", name, sep='')
            continue

        break

    items_list[name][2] -= amount

    if name in order_list:
        order_list[name] += amount
    else:
        order_list[name] = amount
    return True
