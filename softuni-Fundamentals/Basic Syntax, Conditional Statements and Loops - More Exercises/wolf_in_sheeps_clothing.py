animals = input().split(", ")

if animals[-1].strip() == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    animal_position = len(animals) - animals.index("wolf") - 1
    print(f"Oi! Sheep number {animal_position}! You are about to be eaten by a wolf!")