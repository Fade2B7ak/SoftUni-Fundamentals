text = input()
result = ""

while text != "":
    result += text[0]
    text = text.lstrip(text[0])

print(result)
