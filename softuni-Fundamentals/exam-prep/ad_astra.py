import re


data = input()
pattern = r"(\||#)([A-Za-z]+ ?[A-Za-z]+)\1([0-9]{2})\/([0-9]{2,})\/([0-9]{2})\1([0-9]{1,4})\1"

matches = re.findall(pattern, data)
total_calories = 0

for match in matches:
    calories = int(match[5])
    total_calories += calories
days_left = math.floor(total_calories / 2000)
print(f"You have food to last you for: {days_left} days!")

for match in matches:
    food = match[1]
    day = match[2]
    month = match[3]
    year = match[4]
    calories = match[5]
    print(f"Item: {food}, Best before: {day}/{month}/{year}, Nutrition: {calories}")
