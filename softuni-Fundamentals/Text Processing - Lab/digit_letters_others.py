command = input()
letters = []
digits = []
other = []

for char in command:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        other.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(other))