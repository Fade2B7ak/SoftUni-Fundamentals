def grades():
    number_of_rows = int(input())
    list_of_students = []
    list_of_grades = []
    current_row = 1

    for number in range(1, number_of_rows * 2 + 1):
        information = input()
        if current_row % 2 == 0:
            list_of_grades.append(information)
        else:
            list_of_students.append(information)

        current_row += 1
    list_of_grades = [float(i) for i in list_of_grades]

    info_dict = {}

    for name, grade in zip(list_of_students, list_of_grades):
        if name not in info_dict:
            info_dict[name] = grade
        else:
            info_dict[name] = float((info_dict[name] + grade) / list_of_students.count(name))

    for name,grade in info_dict.items():
        if grade >= 4.50:
            print(f"{name} -> {grade:.2f}")


grades()
