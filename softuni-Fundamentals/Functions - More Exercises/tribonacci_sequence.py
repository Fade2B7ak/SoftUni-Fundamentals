def tribonacci_sequence(start, num):
    if num >= 3:
        for number in range(num - 1):
            num = sum(start[-3:])
            start.append(num)
        return start
    else:
        for numb in range(num - 1):
            num = sum(start[-2:])
        return start

start = [1]
numbero = int(input())
print(*tribonacci_sequence(start, numbero))