# 1. Multiplication
# Create a function that gets a number as a parameter, 
# and then prints the multiplication table for that number from 1 to 10. E.g.,
# when the parameter is 12, 
# the first line printed is “1 x 12 = 12” and the last line printed is “10 x 12 = 120.”
print("welcome to multiplication table")


def multiplication(number):
    for n in range(1,11):
        print(number*n)
multiplication(number=int(input("please enter any number")))