# 1. Building Dictionaries from a List
# The code below contains a list of words. Build a dictionary that contains all these words as keys, and their quantities as values. Print the words with their quantities.




wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]


dictionary_wordlist={}
count=1
for n in  wordlist:
    count=count + 1
    dictionary_wordlist[n]=count
    

print(dictionary_wordlist)




fruitbasket = { "apple":3, "banana":5, "cherry":50 }
fruitbasket["apple"]=2
print( fruitbasket )



# for key in fruitbasket:
#    print( "{}:{}".format( key, fruitbasket[key] ))



# print( fruitbasket )
# fruitbasket["mango"] = 1
# print( fruitbasket )


# print( list( fruitbasket.keys() ) )
# items=list( fruitbasket.keys()) 
# print( list( fruitbasket.values() ) )
# print( list( fruitbasket.items() ) )

# print(dict(items))