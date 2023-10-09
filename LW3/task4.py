import json


def start():
    total_profit = 0
    profitable_firms_amount = 0
    firms = []

    with open("firms.txt", encoding="utf-8") as file:
        for line in file:
            firm_data = line[:-1].split()
            firms.append({firm_data[0]: float(firm_data[2]) - float(firm_data[3])})

            if firms[-1][firm_data[0]] >= 0:
                total_profit += firms[-1][firm_data[0]]
                profitable_firms_amount += 1

    if len(firms) == 0:
        print("Файл пуст")
        return

    print("Средняя прибыль фирм:", total_profit / len(firms))
    print(firms)

    with open("firms.json", 'w', encoding="utf-8") as file:
        json.dump(firms, file, ensure_ascii=False)
