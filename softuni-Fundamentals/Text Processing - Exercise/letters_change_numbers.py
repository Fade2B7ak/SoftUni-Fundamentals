data = [element.strip() for element in input().split()]

alphabet = {chr(96 + num): num for num in range(1, 27)}
result = 0
for index in data:
    first_letter = index[0]
    second_letter = index[len(index) - 1:]
    num = int(index[1:len(index) -1])

    if first_letter.isupper():
        current_sum = num / alphabet[first_letter.lower()]
    else:
        current_sum = num * alphabet[first_letter.lower()]

    if second_letter.isupper():
        current_sum -= alphabet[second_letter.lower()]
    else:
        current_sum += alphabet[second_letter.lower()]
    result += current_sum
print(f"{result:.2f}")