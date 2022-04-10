number = int(input())

positive = []
negative = []
sum_of_negatives = 0

for num in range(number):
    current = int(input())
    if current >= 0:
        positive.append(current)
    else:
        negative.append(current)
        sum_of_negatives += current

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum_of_negatives}')
