fire_cells = input().split('#')
water = int(input())
effort = 0
total_fire = 0
fire_stop = []
cell = ''
cell1 = ''
b = ''

for level in range(len(fire_cells)):
    if water <= 0:
        break

    if "High" or "Medium" or "Low" in fire_cells[level]:
        cell = fire_cells[level]
        if "High" in cell:
            b = cell.split()
            cell1 = int(b[2])
            if cell1 >= 81 and cell1 <= 125 and water >= cell1:
                effort += cell1 * 0.25
                water -= cell1
                total_fire += cell1
                fire_stop.append(cell1)
        if "Medium" in cell:
            b = cell.split()
            cell1 = int(b[2])
            if cell1 >= 51 and cell1 <= 80 and water >= cell1:
                effort += cell1 * 0.25
                water -= cell1
                total_fire += cell1
                fire_stop.append(cell1)
        if "Low" in cell:
            b = cell.split()
            cell1 = int(b[2])
            if cell1 >= 1 and cell1 <= 50 and water >= cell1:
                effort += cell1 * 0.25
                water -= cell1
                total_fire += cell1
                fire_stop.append(cell1)

print("Cells:")
for fire in range(len(fire_stop)):
    print(f' - {fire_stop[fire]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {int(total_fire)}')