# from pcinput import getInteger
# num = pcinput( "Please enter a number: " )
# print( "3 divided by {} is {}".format( num, 3/num ) )
# print( "Goodbye!" )



# num = int(input( "Please enter a number: " ))
# if num == 0:
#     print( "Dividing by zero is not allowed" )
# else:
#     print( "3 divided by {} is {}".format( num, 3/num ) )
# print( "Goodbye!" )




# num = int(input( "Please enter a number: " ))
# try:
#     print( "3 divided by {} is {}".format( num, 3/num ) )
# except:
#     print( "Division by zero is not allowed" )
# print( "Goodbye!" )




num = int(input( "Please enter a number: " ))
try:
    print( "3 divided by {} is {}".format( num, 3/num ) )
    print( "3 divided by {}-3 is {}".format( num, 3/(num -3) ) )
except:
    print( "Division by zero is not allowed" )
print( "Goodbye!" )