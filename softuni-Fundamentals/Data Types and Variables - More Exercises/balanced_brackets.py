number_of_lines = int(input())
previous_bracket = ")"
is_balanced = True

for _ in range(number_of_lines):
    random = input()
    if random == chr(40) or random == chr(41):
        if not previous_bracket == random:
            previous_bracket = random
        else:
            is_balanced = False
            print("UNBALANCED")
            break

if is_balanced:
    print("BALANCED")


