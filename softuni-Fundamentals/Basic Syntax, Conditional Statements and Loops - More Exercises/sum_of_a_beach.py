text = input().lower()

listo = ["sand", "water", "fish", "sun"]
counter = 0

for item in listo:
    if item in text:
        word_counter = text.count(item)
        counter += word_counter

print(counter)