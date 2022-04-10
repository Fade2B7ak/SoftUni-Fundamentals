def sum_numbers(a, b):
    return a + b

def subtract(numbers, c):
    return numbers - c


first = int(input())
second = int(input())
third = int(input())
result = subtract(sum_numbers(first, second), third)
print(result)