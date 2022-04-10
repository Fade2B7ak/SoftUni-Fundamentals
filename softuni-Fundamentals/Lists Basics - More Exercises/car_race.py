numbers = input().split()

car_one = 0
car_two = 0

middle = len(numbers) // 2 + 1

for time in numbers[0:middle - 1]:
    car_one += int(time)

    if int(time) == 0:
        car_one = (car_one * 80) / 100

for time in numbers[len(numbers):middle - 1: -1]:
    car_two += int(time)
    if int(time) == 0:
        car_two = (car_two * 80) / 100

if car_one > car_two:
    winner = "right"
    print(f'The winner is {winner} with total time: {car_two:.1f}')
else:
    winner = "left"
    print(f'The winner is {winner} with total time: {car_one:.1f}')