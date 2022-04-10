def multiplication(num1, num2, num3):
    result = num1 * num2 * num3
    if result > 0:
        print("positive")
    elif result == 0:
        print("zero")
    else:
        print("negative")
num1 = int(input())
num2 = int(input())
num3 = int(input())
multiplication(num1, num2, num3)