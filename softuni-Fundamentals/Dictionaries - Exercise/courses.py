course = {}
command = input()
while command != "end":
    current_command = command.split(" : ")
    if current_command[0] not in course:
        course[current_command[0]] = []
    course[current_command[0]].append(current_command[1])

    command = input()

for key, value in course.items():
    print(f"{key}: {len(value)}")
    print(f"-- ", end='')
    print(*value, sep="\n" "-- ")
