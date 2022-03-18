# 2. Sum of two strings
# Write a function that gets as parameters two strings. The function returns the number of characters that the strings have in common.
#  Each character counts only once, e.g., the strings "bee" and "peer" only have one character in common (the letter “e”).
#  You can consider capitals different from lower case letters. Note: the function should return the number of characters that the strings have in common,
#  and not print it. To test the function, you can print the result in your main program.

name="aaahmeet"
result=''.join(sorted(set(name), key=name.index)) #very important part for unreapeatable char to find them!!!!!!!!!!!!!!!!!!!!!!!!!!
print(result)

def sum_of_two_strings(str1,str2):
    string1=str1.lower()
    string2=str2.lower()
    result1=''.join(sorted(set(string1), key=string1.index))
    result2=''.join(sorted(set(string2), key=string2.index))
    print(len(result1)) 
    print(len(result2)) 

sum_of_two_strings("foo","kool")




