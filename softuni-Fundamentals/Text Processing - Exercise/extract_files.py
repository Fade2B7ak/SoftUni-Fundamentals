def extract_file(data):
    needed_info = data[-1].split('.')
    name = needed_info[0]
    extension = needed_info[1]
    print(f"File name: {name}")
    print(f"File extension: {extension}")


file = input().split("\\")
extract_file(file)
