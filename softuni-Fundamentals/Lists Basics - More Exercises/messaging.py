numbers = input().split()
string = input()

output = []

for i in numbers:
    index = 0
    for num in i:
        index += int(num)

    if index > len(string):
        index -= len(string)

    output.append(string[index])
    string = string[:index] + string[index + 1:]

print("".join(output))