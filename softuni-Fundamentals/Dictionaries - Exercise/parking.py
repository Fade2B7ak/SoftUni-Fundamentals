def parking():
    registry_dict = {}
    number = int(input())
    for numb in range(number):
        command = input().split(' ')
        if command[0] == 'register':
            username = command[1]
            license_plate = command[2]
            if username in registry_dict:
                print(f"ERROR: already registered with plate number {license_plate}")
            else:
                registry_dict[username] = license_plate
                print(f"{username} registered {license_plate} successfully")
        elif command[0] == 'unregister':
            username = command[1]
            if username not in registry_dict:
                print(f"ERROR: user {username} not found")
            else:
                registry_dict.pop(username)
                print(f"{username} unregistered successfully")

    for username, license_plate in registry_dict.items():
        print(f"{username} => {license_plate}")


parking()
