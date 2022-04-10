sums_list = input().split(", ")
count_of_beggards = int(input())
collected_money = []
beggars_turn = 0
temp_sum = 0
list_of_digits = []

for index in range(len(sums_list)):
    list_of_digits.append(int(sums_list[index]))

while beggars_turn < count_of_beggards:
    for beggar in range(beggars_turn, len(list_of_digits), count_of_beggards):
        temp_sum += list_of_digits[beggar]
    collected_money.append(temp_sum)
    temp_sum = 0
    beggars_turn += 1

print(collected_money)
