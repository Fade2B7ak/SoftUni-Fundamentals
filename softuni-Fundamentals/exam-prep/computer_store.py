def computer_store():
    command = input()
    taxes = 0.2
    tax = 0
    price_without_tax = 0

    while command not in 'special regular':
        parts_price = float(command)
        if parts_price > 0:
            price_without_tax += parts_price
            tax = price_without_tax * taxes
        else:
            print("Invalid price!")
        command = input()
    total_price = price_without_tax + tax
    if total_price == 0:
        print("Invalid order!")
    else:
        if command == 'special':
            total_price -= total_price * 0.10
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {price_without_tax:.2f}$")
        print(f"Taxes: {tax:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")


computer_store()
