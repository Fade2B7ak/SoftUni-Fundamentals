import math

number_of_people = int(input())
capacity = int(input())

courses = 0

for course in range(1, courses + 1):
    courses = math.ceil(number_of_people / capacity)
    people_left = number_of_people % capacity
    if people_left == 0:
        print(courses)

    elif people_left != 0:
        courses += 1
        print(courses)