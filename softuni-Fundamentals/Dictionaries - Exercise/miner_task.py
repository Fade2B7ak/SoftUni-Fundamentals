def miner():
    resource_dict = {}
    while True:
        command = input()
        if command == "stop":
            break

        quantity = int(input())

        if command not in resource_dict:
            resource_dict[command] = quantity
        else:
            resource_dict[command] += quantity

    for key, value in resource_dict.items():
        print(f"{key} -> {value}")
miner()