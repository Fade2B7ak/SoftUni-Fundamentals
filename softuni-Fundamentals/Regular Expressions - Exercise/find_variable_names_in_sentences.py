import re

text = input()
pattern = r'\b_[A-Za-z0-9]+\b'
matches = re.findall(pattern, text)

match_list = []
for match in matches:
    match_list.append(match[1:])
print(','.join(match_list))
