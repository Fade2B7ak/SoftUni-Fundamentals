import re

reg = r"\d+"
while True:
    text = input()
    if not text:
        break
    matches = re.findall(reg, text, re.MULTILINE)

    for match in matches:
        print(''.join(match), end=' ')
