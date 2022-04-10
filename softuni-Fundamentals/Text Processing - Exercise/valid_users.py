import string


def username(data):
    flag = 0
    needed_elements = string.ascii_letters + string.digits + '-' + '_'
    for name in data:
        flag = 0
        if 3 > len(name) or len(name) > 16:
            flag = 1
        elif len([symbol for symbol in name if symbol in needed_elements]) != len(name):
            flag = 1
        elif flag == 0:
            print(name)


text = input().split(", ")
username(text)
