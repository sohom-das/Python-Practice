num = int(input("Enter a positive integer: "))


###Factorial function###
def factorial(num):
    if num < 0:
        return 0

    elif num == 0:
        return 1

    else:
        # taking initially fact as 1
        fact = 1
        # iterating through range (1 to user number)
        for i in range(1, num + 1):
            fact *= i
            print(i, end=" ")
        print("\nFactorial of", num, "is", fact)


# define a flag variable
flag = False
# prime are greater than 1
if num > 1:
    # iterating through the range (2 to (num-1))
    for x in range(2, num):
        if num % x == 0:
            # if the condition becomes at any point, then set the flag to #true
            flag = True
            # then break out the loop
            break

if flag:
    print(num, "is not a Prime number")
    print(factorial(num))


else:
    print(num, "is a Prime number")