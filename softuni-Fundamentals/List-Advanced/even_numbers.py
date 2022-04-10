numbers = input().split(", ")
numbers = list(map(int, numbers))
even_index = []

for number in range(len(numbers)):
    if numbers[number] % 2 == 0:
        even_index.append(number)

print(even_index)