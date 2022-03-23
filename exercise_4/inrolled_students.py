# 2. Inrolled Students
# A student has the last name, a first name, a date of birth (either a year, month, and day, 
# or a DateTime object if you took the liberty of studying the DateTime module already), and an administration number.
#  A course has a name and a number. Students can enroll in courses. Create a class Student and a class Course. 
# Create several students and several courses. Enroll each student in some of the courses.
#  Display a list of students, showing their number, first name, last name, and age, and per student which courses he or she is enrolled in.


from datetime import datetime

class Student:
     def __init__(self, first_name, last_name, birth ,DateTime,administration_number):

        self.first_name = first_name
        self.last_name = last_name
        self.birth=birth
        self.DateTime=DateTime
        self.administration_number=administration_number


class Course(Student):
      def __init__(self, first_name,last_name, birth ,DateTime,administration_number, number):
        super().__init__(first_name,last_name, birth ,DateTime,administration_number)
        self.courselist = []
        self.course_total=[]
        self.number=number

      def enroll(self, course):
        self.courselist.append(course)
    

      def course_program(self):
          return  "name: " + self.first_name +" "+ "surname: " + self.last_name +" "+"birth day: " +\
          self.birth +" "+ "admisnitration number: "+str(self.administration_number) +" "+"Date: "+ str(self.DateTime)+" "+"Course name: "+str(self.courselist)
        

student_infos = Course("frank","johnasen","02/03/1990",datetime.now(),12,34)
student_infos2=Course("william" ,"goals" ,"12/05/1991" ,datetime.now(),31,65)


print(student_infos.first_name)
print(student_infos.DateTime)  

student_infos.enroll("code matrix")
student_infos2.enroll("cybertekschool")

print(student_infos.courselist)  


print(student_infos.course_program())
print(student_infos2.course_program())

