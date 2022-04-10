text = input()
vowels_list = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]

no_vowels = "".join([x for x in text if x not in vowels_list])
print(no_vowels)