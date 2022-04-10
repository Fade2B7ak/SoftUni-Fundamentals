number = int(input())
numbers_list = []

for i in range(number):
    current = int(input())
    numbers_list.append(current)

filtered_word = input()
filtered = []

for current_number in numbers_list:
    if filtered_word == 'even' and current_number % 2 == 0:
        filtered.append(current_number)
    elif filtered_word == 'odd' and current_number % 2 != 0:
        filtered.append(current_number)
    elif filtered_word == 'positive' and current_number >= 0:
        filtered.append(current_number)
    elif filtered_word == 'negative' and current_number < 0:
        filtered.append(current_number)

print(filtered)