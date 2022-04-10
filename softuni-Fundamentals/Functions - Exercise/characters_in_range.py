def two_character(start, stop):
    for letter in range(ord(start) + 1, ord(stop)):
        print(chr(letter), end=' ')

start = input()
stop = input()
two_character(start, stop)

