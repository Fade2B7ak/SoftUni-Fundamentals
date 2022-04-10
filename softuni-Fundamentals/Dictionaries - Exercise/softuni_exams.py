exam_result = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    if "banned" not in command:
        command = command.split('-')
        username = command[0]
        language = command[1]
        points = int(command[2])

        if language not in exam_result:
            exam_result[language] = {username: points}
            submissions[language] = 1
        else:
            if username not in exam_result[language]:
                exam_result[language][username] = points
                submissions[language] += 1
            else:
                if points > exam_result[language][username]:
                    exam_result[language][username] = points
                    submissions[language] += 1
                else:
                    submissions[language] += 1
    elif "banned" in command:
        command = command.split('-')
        username = command[0]
        for key, values in exam_result.items():
            if username in values:
                del exam_result[key][username]

print("Results:")
for key, value in exam_result.items():
    for v in value:
        print(f"{v} | {value[v]}")
print("Submissions:")
for key in submissions:
    print(f"{key} - {submissions[key]}")
