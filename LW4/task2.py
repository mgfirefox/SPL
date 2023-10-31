import vehicle


def start():
    routes = [
        "Минск-Брест",
        "Минск-Гродно",
        "Минск-Гомель",
        "Минск-Витебск",
        "Минск-Могилёв",
    ]

    while True:
        try:
            user_choice = int(input('''1. Вывести доступные маршруты
2. Найти самую быструю и экономичную поездку
3. Записать самую быструю и экономичную поезду в файл
0. Выход        
'''))
        except ValueError:
            print("Введите целое число от 2 до 3 или 0")
            continue

        if user_choice < 0 or user_choice > 3:
            continue

        if user_choice == 0:
            break
        elif user_choice == 1:
            print("Доступные маршруты:", routes)
        elif user_choice == 2:
            fastest_route_information, most_economical_route_information = get_route_information(routes)

            if fastest_route_information is None or most_economical_route_information is None:
                continue

            print("Самая быстрая поездка:")
            print(get_route_information_as_str(fastest_route_information))

            print("Самая экономичная поездка:")
            print(get_route_information_as_str(most_economical_route_information))
        else:
            with open("routes.txt", "w", encoding="utf-8") as file:
                fastest_route_information, most_economical_route_information = get_route_information(routes)

                if fastest_route_information is None or most_economical_route_information is None:
                    continue

                file.write("Самая быстрая поездка:\n")
                file.write(get_route_information_as_str(fastest_route_information) + '\n')

                file.write("Самая экономичная поездка:\n")
                file.write(get_route_information_as_str(most_economical_route_information) + '\n')


def get_route(routes):
    start_point = input("Введите начальную точку маршрута: ")
    end_point = input("Введите конечную точку маршрута: ")

    for route in routes:
        if route.find(start_point) != -1 and route.find(end_point) != -1:
            return route
    else:
        return None


def get_route_information(routes):
    route = get_route(routes)

    if route is None:
        print("Нет информации для данного маршрута")
        return None, None

    fastest_route_information = ("Автомобиль", vehicle.Car.information[route])
    most_economical_route_information = fastest_route_information

    if vehicle.Train.information[route][1] < fastest_route_information[1][1]:
        fastest_route_information = ("Поезд", vehicle.Train.information[route])
    if vehicle.Train.information[route][0] < fastest_route_information[1][0]:
        most_economical_route_information = ("Поезд", vehicle.Train.information[route])

    if vehicle.Plane.information[route][1] < fastest_route_information[1][1]:
        fastest_route_information = ("Самолёт", vehicle.Plane.information[route])
    if vehicle.Plane.information[route][0] < fastest_route_information[1][0]:
        most_economical_route_information = ("Самолёт", vehicle.Plane.information[route])

    return fastest_route_information, most_economical_route_information


def get_route_information_as_str(route_information):
    return (f"{route_information[0]}: цена {route_information[1][0]}р,"
            f" длительность {route_information[1][1] // 60}ч {route_information[1][1] % 60}мин")
