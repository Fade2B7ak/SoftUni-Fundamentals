def contact_book_information(number_of_lines, contact_dict):
    for line in range(number_of_lines):
        name = input()
        if name not in contact_dict:
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {contact_dict[name]}")

    return True


def phonebook():
    contact_dict = {}
    condition = False

    while True:
        information = input().split("-")
        if information[0].isdigit():
            condition = contact_book_information(int(information[0]), contact_dict)
        else:
            contact_dict[information[0]] = information[1]

        if condition:
            break


phonebook()
