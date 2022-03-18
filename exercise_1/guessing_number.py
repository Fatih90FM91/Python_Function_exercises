# 3. Guessing number
# Write a guessing number function that holds a random number between 1 and 10 and get a parameter number. The return for that function will be :

# "Too big" if the parameter number is bigger than the held number.
# "Too small" if the parameter number is smaller than the held number.
# "You are SUPER" if the parameter number is the same as the held number.
# Enter the parameter number via the terminal with a help of the input method.




import random


guess_num=int(input("do guessing any number here! \n"))

def guessing_num(number):
    n=random.randint(1,11)
    if  number>n:
        print("Too Big!!")
    elif number<n:
        print("Too small!!")
    elif number==n:
        print("You are SUPER!!!")
    else:
        print("Enter vaid number..!!")

guessing_num(guess_num)