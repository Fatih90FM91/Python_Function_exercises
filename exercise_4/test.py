fruitset = { "apple", "banana", "cherry" }
print( fruitset )

helloset = set( "hello world" )
print( helloset )



fruitset = { "apple", "banana", "cherry", "durian", "mango" }
for element in fruitset:
  print( element )
print()
fruitlist = list( fruitset )
fruitlist.sort()
for element in fruitlist:
  print( element )


fruitset.add("hunter")
print(fruitset)

fruitset.update(["love","love","love","love","love","love","going","life"])
print(fruitset)
fruitset.remove("life")
print(fruitset)
fruitset.discard("love")
print(fruitset)
# fruitset.clear()
# print(fruitset)


fruitset = { "apple", "banana", "cherry", "durian", "mango" }
while len( fruitset ) > 0:
    print( fruitset.pop() ) 



fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry", "durian" }
fruitunion = fruit1.union( fruit2 )
print( fruitunion )
fruitunion = fruit1 | fruit2
print( fruitunion )

print()

fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry", "durian" }
fruitintersection = fruit1.intersection( fruit2 )
print( fruitintersection )
fruitintersection = fruit1 & fruit2
print( fruitintersection )


print()
fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry", "durian" }
fruitdifference = fruit1.difference( fruit2 )
print( fruitdifference )
fruitdifference = fruit1 - fruit2
print( fruitdifference )
fruitdifference = fruit2 - fruit1
print( fruitdifference )


print()
fruit1 = { "apple", "banana", "cherry" }
fruit2 = { "banana", "cherry" }
print( fruit1.isdisjoint( fruit2 ) )
print( fruit1.issubset( fruit2 ) )
print( fruit2.issubset( fruit1 ) )
print( fruit1.issubset( fruit1 ) )
print( fruit1.issuperset( fruit2 ) )
print( fruit2.issuperset( fruit1 ) )
print( fruit1.issuperset( fruit1 ) )