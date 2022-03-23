class Point:
    pass
p = Point()
print( type( p ) )



class Point:
    def __init__( self ):
        self.x = 0.0
        self.y = 0.0
p = Point()
print( "({}, {})".format( p.x, p.y ) )


from math import sqrt
class Point:
    def __init__( self , x=0.0 , y=0.0 ):
        self.x = x
        self.y = y
    def distance_from_origin( self ):
        return sqrt( self.x * self.x + self.y * self.y )
p = Point( 3.5, 5.0 )
print( p.distance_from_origin() )


print()

from math import sqrt
class Point:
    def __init__( self , x=0.0 , y=0.0 ):
        self.x = x
        self.y = y

    def translate( self , shift_x , shift_y ):
        self.x += shift_x
        self.y += shift_y
p = Point( 3.5, 5.0 )
p.translate( -3, 7 )
print( p )


print()

# class Person:
#     def __init__( self , firstname , lastname , age ):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age

#     def underage( self ):
#         return self.age < 18

# class Student( Person ):
#     pass

# albert = Student( "Albert", "Applebaum", 19 )
# print( albert.firstname )
# print( albert.age )
# print( albert.underage() )

print()
print()
print()

class Person:
    def __init__(self, firstname, lastname, age):


        self.firstname = firstname
        self.lastname = lastname
        self.age = age

def underage(self):
    return self.age < 18

class Student(Person):
    def __init__(self, firstname, lastname, age, program):
        super().__init__(firstname, lastname, age)
        self.courselist = []
        self.program = program

    def underage(self):
        return self.age < 21

    def enroll(self, course):
        self.courselist.append(course)
        
albert = Student("Albert", "Applebaum", 19, "CSAI")
print(albert)
print(albert.underage())
print(albert.program)
albert.enroll("Methods of Rationality")
albert.enroll("Defense Against the Dark Arts")
print(albert.courselist)