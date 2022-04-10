text = input()
power = 0
output = ''

for symbol in range(len(text)):
    if text[symbol] != ">" and power > 0:
        power -= 1
    elif text[symbol] == ">":
        power += int(text[symbol + 1])
        output += text[symbol]
    else:
        output += text[symbol]

print(output)
