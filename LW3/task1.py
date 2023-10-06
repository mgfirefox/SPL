def start():
    file1 = open("file1.txt", 'w+')

    while True:
        string = input("Введите строку (для выхода введите пустую строку): ")

        if len(string) == 0:
            break
        else:
            file1.write(string + '\n')

    file1.seek(0)
    file2 = open("file2.txt", "w+")

    for string in file1:
        if string[:-1].isalpha() and len(string.split()) == 1:
            file2.write(string)

    file1.close()
    file2.seek(0)

    longest_words = [""]
    for word in file2:
        word = word[:-1]

        if len(word) > len(longest_words[0]):
            longest_words.clear()
            longest_words.append(word)
        elif len(word) == len(longest_words[0]):
            longest_words.append(word)

    if len(longest_words) > 1:
        print("Самые длинные слова:", longest_words)
    elif longest_words[0] != "":
        print("Самое длинное слово:", longest_words[0])
    else:
        print("Файл пуст. Длинное слово не найдено")

    file2.close()
