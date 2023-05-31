def factorial(x):

    #A recursive function to find the the factorial of a number.
    if  x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    num = 2

    print("The factorial of ", num, "is", factorial(num))
