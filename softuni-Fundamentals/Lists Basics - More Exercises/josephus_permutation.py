numbers = input().split()
number_k = int(input())

executed_ppl = []
next_person = number_k - 1
current_dead = next_person

while numbers:
    if number_k >= len(numbers):
        current_dead = current_dead % len(numbers)

    executed_ppl.append(numbers.pop(current_dead))

    if numbers:
        current_dead = (current_dead + next_person) % len(numbers)

print(f'[{",".join(executed_ppl)}]')