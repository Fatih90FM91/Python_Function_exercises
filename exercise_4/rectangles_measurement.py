# 1. Rectangles Measurement
# Create a version of the Rectangle class that is safe by assuring that both width and height are positive values (how you do that is up to you).
#  Expand it with methods that calculate its surface area and its circumference.
#  Also, provide a method that returns the bottom-right corner of the rectangle as a Point.
#  Finally, create a method that gets a second Rectangle object as a parameter,
#  and returns the overlapping area of the two rectangles as a new Rectangle object (the last one is much harder than the other ones).

class Rectangle:
       def __init__(self, width, height,a,b,c):


        self.width = width
        self.height = height
        self.a=a
        self.b=b
        self.c=c

       def calculate_surface_area(self):

           return self.width*self.height

       def calculate_circumference(self):

           return self.a + self.b + self.c


result = Rectangle(10,10,4,4,4)


print(f"This is  circumference of rectangle : {result.calculate_surface_area()}")
print(f"This is  circumference of rectangle : {result.calculate_circumference()}")
      
