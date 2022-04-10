import re

text = input()
special_word = input()

pattern = rf'\b{special_word}\b'

result = re.findall(pattern, text, re.IGNORECASE)

print(len(result))
