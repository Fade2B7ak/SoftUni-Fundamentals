def company():
    company_name_dict = {}
    command = input()

    while not command == "End":
        current_command = command.split(" -> ")
        if current_command[0] not in company_name_dict:
            company_name_dict[current_command[0]] = []
        if current_command[1] not in company_name_dict[current_command[0]]:
            company_name_dict[current_command[0]].append(current_command[1])

        command = input()

    for companya, id in company_name_dict.items():
        print(f"{companya}")
        print(f"-- ", end="")
        print(*id, sep="\n" "-- ")


company()
