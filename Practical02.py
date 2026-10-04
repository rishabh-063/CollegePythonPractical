# perform creation, traversal and manipulation of python collections (lists, tuple, sets, dictonary).
numbers = [10,20,30]
point = (1,2,3)
colors = {'red','green','blue'}
student = {'name':"Asha","age":20}
numbers.append(40)
student["courese"] = "python"
print(numbers)
print(point)
print(colors)
print(student)

# Create a classm constructor, objects and instance methods.
class Student: 
    def __int__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("name", self.name)
        print("marks", self.marks)
s = Student("Asha",20)
s.display()

# Demonstrate inheritance, method overriding.
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
for a in [Dog(),Cat()] :
    a.sound()

# method overloading.
class Calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c
cal = Calculator()
print(cal.add(2,3))
print(cal.add(2,3,4))

# Create a user-defined module and demonstrate reusable functions and encapsulation

from utility import percentage
print("Percentage:",percentage([80,75,90,85]))