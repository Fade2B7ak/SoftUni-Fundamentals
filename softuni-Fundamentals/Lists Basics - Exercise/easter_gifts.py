list_of_gits = input().split()

while True:
    command = input()
    if command == 'No Money':
        break

    command = command.split()
    if command[0] == 'OutOfStock':
        for gift in range(len(list_of_gits)):
            if str(list_of_gits[gift]) == str(command[1]):
                list_of_gits[gift] = 'None'

    elif command[0] == 'Required':
        if 0 < int(command[2]) < len(list_of_gits):
            list_of_gits[int(command[2])] = command[1]

    elif command[0] == 'JustInCase':
        list_of_gits[len(list_of_gits) - 1] = command[1]

for gift1 in list_of_gits:
    if not gift1 == 'None':
        print(gift1, end=' ')