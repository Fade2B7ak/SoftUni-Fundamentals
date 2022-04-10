base_list = input().split(' ')
end_list = []

for number in base_list:
    final_number = round(float(number))
    end_list.append(final_number)
print(end_list)