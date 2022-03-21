# 5. Palindrome
# Given a string, write a python function to check if it is palindrome or not.
#  A string is said to be palindrome if the reverse of the string is the same as string.
#  For example, “radar” is a palindrome, but “radix” is not a palindrome.



palindrome_word=input("please enter any word..\n").lower()

print(palindrome_word[::-1])

def reversed_function(reverse_word):
    return reverse_word[::-1]


print(reversed_function(palindrome_word))

reversed_word=reversed_function(palindrome_word)

if reversed_word == palindrome_word:
    print("Palindrome....")
else:
    print("Not Palindrome..")
