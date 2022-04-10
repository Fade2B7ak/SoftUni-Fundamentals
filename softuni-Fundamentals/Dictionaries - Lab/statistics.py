products = {}

command = input()

while command != "statistics":
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])

    if product in products.keys():
        products[product] += quantity
    else:
        products[product] = quantity

    command = input()

count = len(products.keys())
total = sum(products.values())

print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f"Total Products: {count}")
print(f"Total Quantity: {total}")
