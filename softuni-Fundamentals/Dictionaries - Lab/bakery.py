elements = input().split(" ")
bakery = {}

for good in range(0, len(elements), 2):
    key = elements[good]
    value = elements[good + 1]
    bakery[key] = int(value)
print(bakery)