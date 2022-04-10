key = int(input())
number_of_lines = int(input())
decrypting_word = ""

for letters in range(number_of_lines):
    letter = input()
    new_letter = ord(letter) + key
    decrypting_word += chr(new_letter)

print(decrypting_word)