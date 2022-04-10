list_input = input().split(' ')
new_list = []

for index in list_input:
    current_value = abs(float(index))
    new_list.append(current_value)

print(new_list)