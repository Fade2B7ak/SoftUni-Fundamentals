x = int(input())
y = int(input())


print("Before:")
print(f'a = {x}')
print(f'b = {y}')
x, y = y, x
print("After:")
print(f'a = {x}')
print(f'b = {y}')