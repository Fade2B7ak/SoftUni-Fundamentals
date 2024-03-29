def the_lift():
    people = int(input())
    ppl = people
    state_of_lift = input().split()
    wagon_space = 4
    sum_places = sum([int(num) for num in state_of_lift])
    free_space = len(state_of_lift) * wagon_space - sum_places

    for space in range(len(state_of_lift)):
        if int(state_of_lift[space]) <= 4 and ppl >= 4:
            ppl -= wagon_space - int(state_of_lift[space])
            state_of_lift[space] = str(wagon_space)
        elif int(state_of_lift[space]) < 4 and ppl < 4:
            state_of_lift[space] = str(int(state_of_lift[space]) + ppl)
            ppl = 0
            break


    if ppl == 0 and free_space > ppl:
        print("The lift has empty spots!")
        print(' '.join(state_of_lift))
    elif ppl > 0:
        print(f"There isn't enough space! {ppl} people in a queue!")
        print(' '.join(state_of_lift))
    else:
        print(' '.join(state_of_lift))

the_lift()
