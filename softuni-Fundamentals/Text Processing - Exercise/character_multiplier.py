def sum_func(first_word, second_word):
    total_sum = 0

    for symbol in range(len(first_word)):
        if symbol < len(second_word):
            total_sum += ord(first_word[symbol]) * ord(second_word[symbol])
        else:
            total_sum += ord(first_word[symbol])

    return total_sum


def character(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = sum_func(first_word, second_word)
    else:
        result = sum_func(second_word, first_word)

    print(result)


multi = input().split()
character(multi[0], multi[1])
