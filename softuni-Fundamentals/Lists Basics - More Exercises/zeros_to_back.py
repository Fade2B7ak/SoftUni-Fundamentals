string_list = input().split(", ")
digit = []
zeros = []

for number in string_list:
    number = int(number)
    if not number == 0:
        digit.append(number)
    else:
        zeros.append(number)

final_list = digit + zeros
print(final_list)