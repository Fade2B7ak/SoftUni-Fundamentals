def data_type(data):
    if data == "int":
        data = int(input())
        data *= 2
        print(data)
    elif data == "real":
        data = float(input())
        data *= 1.5
        print(f"{data:.2f}")
    elif data == "string":
        data = input()
        print(f"${data}$")
type = input()
data_type(type)