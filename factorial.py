def factorial(x):

    #A recursive function to find the the factorial of a number.
    if  x == 0:
        return 1
    else:
        return x * factorial(x - 1)
num = 5
result = factorial(num)
print("The factorial of ", num, "is", result)