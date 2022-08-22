list_of_numbers = input().split()
final_list = []

for num in list_of_numbers:
    final_list.append(int(num))

number = int(input())

for smallest in range(number):
    final_list.remove(min(final_list))


print(*final_list, sep =', ')

#Functional Solving
def survival(numbers_list, numbers_to_removes):
    final_list = []

    for numb in numbers_list:
        final_list.append(int(numb))

    for smallest in range(numbers_to_removes):
        final_list.remove(min(final_list))

    print(*final_list, sep=", ")


survival(numbers_list=input().split(), numbers_to_removes=int(input()))
