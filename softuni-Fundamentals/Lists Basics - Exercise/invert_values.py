number = input().split()
oposite_numbers = []

for index in range(len(number)):
    oposite_number = -int(number[index])
    oposite_numbers.append(oposite_number)
print(oposite_numbers)