import random


def start():
    x = random.randint(1, 10)
    print("Количество столбцов:", x)
    y = random.randint(1, 10)
    print("Количество строк:", y)
    i = random.randint(1, x)
    j = random.randint(1, x)
    print("i = ", i, ", j = ", j, sep='')
    i -= 1
    j -= 1
    
    matrix = [[random.randint(-1000000000, 1000000000) for _ in range(x)] for __ in range(y)]
    for row in matrix:
        print(row)
    print()

    if i != j:
        for row in matrix:
            row[i], row[j] = row[j], row[i]

    print("Столбцы", i + 1, 'и', j + 1, "поменялись местами:")
    for row in matrix:
        print(row)
