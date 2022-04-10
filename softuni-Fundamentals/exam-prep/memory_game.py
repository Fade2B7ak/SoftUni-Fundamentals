sequence = input().split()
count_of_moves = 0
command = input()
while not command == "end":
    count_of_moves += 1
    first_element = int(command.split()[0])
    second_element = int(command.split()[1])
    if first_element == second_element or first_element < 0 or second_element < 0 or first_element >= len(
            sequence) or second_element >= len(sequence):
        sequence.insert(int(len(sequence) / 2), f"-{str(count_of_moves)}a")
        sequence.insert(int(len(sequence) / 2), f"-{str(count_of_moves)}a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence[first_element] == sequence[second_element]:
        print(f"Congrats! You have found matching elements - {sequence[first_element]}!")
        x = sequence.pop(first_element)
        sequence.remove(x)
    elif sequence[first_element] != sequence[second_element]:
        print("Try again!")
    if len(sequence) == 0:
        print(f"You have won in {count_of_moves} turns!")
        break
    command = input()
if command == 'end':
    print("Sorry you lose :(\n"
          f"{' '.join(sequence)}")
