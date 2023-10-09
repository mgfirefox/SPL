def start():
    total_sum = 0
    is_cheap_jewelry_found = False
    jewelry = {}

    with open("jewelry.txt", encoding="utf-8") as file:
        for line in file:
            jewelry_data = line[:-1].split()
            jewelry[jewelry_data[0]] = float(jewelry_data[1])
            total_sum += jewelry[jewelry_data[0]]

            if jewelry[jewelry_data[0]] < 100:
                if not is_cheap_jewelry_found:
                    is_cheap_jewelry_found = True
                    print("Ювелирные украшения дешевле 100 рублей:")

                print(jewelry_data[0], '—', jewelry_data[1])

    if len(jewelry) == 0:
        print("Файл пуст")
        return
    if not is_cheap_jewelry_found:
        print("Ювелирные украшения дешевле 100 рублей не найдены")

    print("Средняя стоимость ювелирных украшений:", total_sum / len(jewelry))
