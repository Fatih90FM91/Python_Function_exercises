# print("hello world!!")
# x=lambda a:a+10
# print(x(10))

my_num=int(input("please enter any number.."))
import random
rand_number=random.randint(1,10)
print("compunter number " +str(rand_number))

if my_num==rand_number:
    print("you win..")
else:
    print("you lose..")