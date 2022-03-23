# 4. Extending Measurement
# Rectangle and a Square can be considered shapes. There are, of course,
#  different kinds of shapes that are defined differently but share with rectangles and squares that they have an area and circumference. 
# Define an interface class Shape, of which Rectangle and Square are sub(sub)classes.
#  Also, define a class Circle that you derive from Shape.

from cmath import pi


class Rectangle:
      def __init__(self, width, height,a,b,c):


        self.width = width
        self.height = height
        self.a=a
        self.b=b
        self.c=c


class Square:  
      def __init__(self, width, height,a,b,c,d):


        self.width = width
        self.height = height
        self.a=a
        self.b=b
        self.c=c
        self.d=d  


class Circle:  
      def __init__(self, r):
         self.r = r
      



class Shape(Rectangle,Square,Circle):
     def __init__(self,width, height,a,b,c,d,r):
         super().__init__( width, height,a,b,c)
         self.d=d
         self.r=r
            

     def area_triangle(self):
        return self.width*self.height

     def circumference_triangle(self):
         return self.a+self.b+self.c   

     def area_square(self):
         return self.a*self.b

     def circumference_square(self):
         return 2*(self.a + self.b)

     def area_circle(self):
        #  pi_num=3,14
         return  pi*(self.r*self.r)

     def circumference_circle(self):
        #  pi_num=3,14
         return 2*pi*self.r



shape_result =Shape(10,10,4,4,4,6,8)
       
            

print(shape_result.a)
print(shape_result.area_triangle())
print(shape_result.r)

print(shape_result.area_circle())

           
 

        
        
