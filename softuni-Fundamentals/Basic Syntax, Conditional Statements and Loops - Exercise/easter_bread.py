budget = float(input())
price_for_flour = float(input())


egg_price = price_for_flour * 0.75
milk_price = (price_for_flour * 1.25) / 4

bread_price = price_for_flour + egg_price + milk_price

loaves = 0
colored_eggs = 0

while budget >= bread_price:
    loaves += 1
    budget -= bread_price
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')