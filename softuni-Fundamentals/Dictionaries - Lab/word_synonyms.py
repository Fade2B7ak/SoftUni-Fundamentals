count = int(input())
dictionary = {}

for number in range(count):
    word = input()
    synonym = input()

    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for word in dictionary:
    synonym = ", ".join(dictionary[word])
    print(f"{word} - {synonym}")