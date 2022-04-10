number_of_lines = int(input())
capacity = 0

for _ in range(number_of_lines):
    litters = int(input())

    if litters + capacity <= 255:
        capacity += litters
        continue

    print("Insufficient capacity!")

print(capacity)