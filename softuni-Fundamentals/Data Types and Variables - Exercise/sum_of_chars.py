numbers = int(input())
total_sum = 0

for n in range(numbers):
    char = input()
    total_sum += ord(char)

print(f'The sum equals: {total_sum}')
