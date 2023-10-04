def start():
    items_list = [1612, 49, "hello", 6, 19, "world"]
    print(items_list)

    for i in range(len(items_list)):
        if isinstance(items_list[i], int):
            if items_list[i] % 2 == 0:
                digits_sum = 0

                for digit in str(items_list[i]):
                    digits_sum += int(digit)

                print("Число", items_list[i], "четное. Сумма его цифр равна", digits_sum)
            else:
                print("Число", items_list[i], "нечетное. Оно заменено на 1")
                items_list[i] = 1
        else:
            vowels_amount = 0
            consonants_amount = 0
            for letter in items_list[i]:
                if (letter == 'a' or letter == 'e' or letter == 'i'
                        or letter == 'o' or letter == 'u' or letter == 'y'):
                    vowels_amount += 1
                else:
                    consonants_amount += 1

            print("Количество гласных в слове ", items_list[i], ": ",
                  vowels_amount, ", согласных — ", consonants_amount, sep='')

    print(items_list)
# or letter == 'а' or letter == 'е' or letter == 'ё' or letter == 'и' or letter == 'о'
# or letter == 'у' or letter == 'ы' or letter == 'ю' or letter == 'э' or letter == 'я'
