# 2. Building Dictionaries from a String
# The code block below contains a string that is a list of words, separated by commas. 
# Build a dictionary that contains all these words as keys, and how often they occur as values. 
# Then print the words with their quantities.


text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

dict_text={}
count =0
for n in text.split(","):
    print(n)
    count=count+1
    dict_text[n]=count


print(dict_text)