info = input()
judge_dict = {}
baned_list = []
submissions = {}
while info != 'exam finished':
    info = info.split('-')
    username = info[0]
    language = info[1]
    if language == 'banned':
        baned_list.append(username)
    else:
        if username not in judge_dict.keys():
            points = int(info[2])
            judge_dict[username] = {language: points}
            if language not in submissions.keys():
                submissions[language] = 1
            elif language in submissions.keys():
                submissions[language] += 1
            points = int(info[2])
        else:
            if language not in submissions.keys():
                submissions[language] = 1
            elif language in submissions.keys():
                submissions[language] += 1
            points = int(info[2])
            if language not in judge_dict[username].keys():
                judge_dict[username][language] = points

            if points > judge_dict[username][language]:
                judge_dict[username][language] = points
    info = input()
print("Results:")
for key, value in judge_dict.items():
    if key not in baned_list:
        for key_1, value_1 in judge_dict[key].items():
            print(f'{key} | {value_1}')
print('Submissions:')
for key, value in submissions.items():
    print(f'{key} - {value}')