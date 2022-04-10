word = input()

word_list = []


for letter in range(len(word)):
    if word[letter].isupper():
        word_list.append(letter)

print(word_list)