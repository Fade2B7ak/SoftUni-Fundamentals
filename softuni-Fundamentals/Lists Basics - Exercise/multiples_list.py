factor_number = int(input())
count = int(input())

list_of_numbers = []

for multiplayer in range(1, count + 1):
    list_of_numbers.append(factor_number * multiplayer)
print(list_of_numbers)