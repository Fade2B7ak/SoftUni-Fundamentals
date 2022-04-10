def emo_text(text):
    result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ':' and text[i + 1] != ' ']
    print('\n'.join(result))


tex = input()
emo_text(tex)
