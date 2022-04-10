def perfect(number):
    sum = 0

    for i in range(1, number):
        if(number % i == 0):
            sum += i
    if(sum == number):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

numb = int(input())
perfect(numb)