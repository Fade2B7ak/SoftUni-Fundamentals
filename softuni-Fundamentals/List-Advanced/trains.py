train_length = int(input())
train = [0 for i in range(train_length)]

command = input()

while command != "End":
    explode = command.split(" ")
    current = explode[0]

    if current == "add":
        num_people = int(explode[1])
        train[- 1] += num_people
    if current == "insert":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] += num_people
    elif current == "leave":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] -= num_people
    command = input()

print(train)