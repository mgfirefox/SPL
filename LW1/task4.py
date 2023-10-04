def start():
    dictionary = {"alter": 5, "digit": 5, "current": 7, "vowel": 5, "consonant": 9, "fridge": 6}
    print(dictionary)

    print("Сортировка словаря в порядке возрастания:")
    print(sorted(dictionary, key=dictionary.get))

    print("Сортировка словаря в порядке убывания:")
    print(sorted(dictionary, key=dictionary.get, reverse=True))
