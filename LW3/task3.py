def start():
    subjects = {}

    with open("subjects.txt") as file:
        for line in file:
            subject_data = line[:-1].split()

            if len(subject_data) > 1:
                subjects[subject_data[0]] = 0
                for i in range(1, len(subject_data)):
                    subjects[subject_data[0]] += int(subject_data[i][:-4])

    if len(subjects) == 0:
        print("Файл пуст")
    else:
        print(subjects)
