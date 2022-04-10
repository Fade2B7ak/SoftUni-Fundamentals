end = False
count_of_coffees = 0

while not end:
    event = input()
    if count_of_coffees > 5:
        print("You need extra sleep")
        break
    elif event == 'END':
        end = True
        break

    elif event == 'dog' or event == 'coding' or event == 'movie' or event == 'cat':
        count_of_coffees += 1

    elif event == 'DOG' or event == 'CODING' or event == 'MOVIE' or event == 'CAT':
        count_of_coffees += 2

if count_of_coffees <= 5:
    print(count_of_coffees)