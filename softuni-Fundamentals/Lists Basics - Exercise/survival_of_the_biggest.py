list_of_numbers = input().split()
final_list = []

for num in list_of_numbers:
    final_list.append(int(num))

number = int(input())

for smallest in range(number):
    final_list.remove(min(final_list))


print(*final_list, sep =', ')