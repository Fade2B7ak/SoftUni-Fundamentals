def ceaser_cipher(text):
    encrypted_letter = [chr(ord(symbol) + 3) for symbol in text]
    print(''.join(encrypted_letter))


text = input()
ceaser_cipher(text)
