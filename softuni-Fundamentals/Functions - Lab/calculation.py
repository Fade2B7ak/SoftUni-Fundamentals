def calculator(first_number, second_number, operator):
    if operator == 'add':
        return first_number + second_number
    elif operator == 'subtract':
        return first_number - second_number
    elif operator == 'multiply':
        return first_number * second_number
    elif operator == 'divide':
        return int(first_number / second_number)

print(calculator(operator=input(), first_number=int(input()), second_number=int(input())))