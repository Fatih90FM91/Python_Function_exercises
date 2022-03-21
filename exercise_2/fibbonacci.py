# 3. Fibonacci
# Write a Fibonacci sequence using python. 
# A Fibonacci sequence is an infinite series of numbers that are created by adding the last two numbers in the series. 
# A series would start with the numbers 1 and 1 in place, followed by 1 (0+1). 2(1+1), 3(1+2), 5(3+2), etc.. 

# 0 1 1 2 3 5 8 13 21 ....


list=[0,1]

number=int(input("please enter any number...\n"))
# result=""
for n in range(0,number):
    result=list[n]+list[n+1]
    list.append(result)

print(list)