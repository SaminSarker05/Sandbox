# OBJECT --> instance of a class
# everything in python is a class
# method --> functions belonging to a class instance or class itself
# - acts on objects or classes
# CLASS --> has attributes and methods
# self --> reference to a class instance/object
# cls --> reference to class 
# - use self to refer to an instances methods and attributes
# - every method takes a self argument which is invisible passed when an object method called
# cls --> represents class itself as a whole

# MODULE --> python file 
# optional -m tag specifies which python file to run

# INHERITENCE 
# - parent and child classes
# - inherit parents methods and attributes
# - can NOT OVERLOAD FUNCTIONS IN PYTHON
# - can OVERRIDE DERIVED CLASSES
# to inherit from some parent class use --> class class_name(parent_class, parent_class, ...)
# specify parent classes in parenthesis
# super().__init__() --> calls the parent class constructor
# super reference to superclass or parent class

# f"{argument}"

class Math:
  # STATIC methods --> does not have access to class attributes/methods, DOES NOT CHANGE ANYTHING
  # to denote use function decorator
  # to use className.staticMethod()
  @staticmethod
  def add(n1, n2):
    return n1 + n2

# to use do not need to make a class instance can directly call method with class name
# print(Math.add(5, 4))

# we can have (global) class attributes by definiing variable within class but not in function
# to refer to (global) class attribute class_name.global_attribute --> shared among all class instances
class Person:
  number_of_people = 0
  def __init__(self, name):
    self.name = name
    Person.number_of_people += 1  # can increment global class attribute in constructor
  
  # can have class methods that don't act on class instances but the class itself
  # denote by function decorator
  @classmethod
  def number_of_people_(cls): # takes cls argument --> reference to class
    return cls.number_of_people 

  @classmethod
  def add_person(cls):
    cls.number_of_people += 1


class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.string = "samin was here"
  
  def speak(self):
    print(f"I don't know what I am {self.string}")


class Dog(Pet):
  def __init__(self, name, age):
    super().__init__(name, age)  # call parent constructor with required arguments for constructor
  def bark(self):
    print("bark")


class Fish(Pet):
  # if child class does not override an inherited method then parents method is used
  # if parent constructor requires arguments we must pass them up
  def __init__(self, name, age):
    # super() function used to refer to parent or super class
    super().__init__(name, age, color)  # call parent classes constructor
    self.color = color  # can set additional class attributes


class Dog:
  # class constructor --> not necessary
  def __init__(self, name): # can accept arguments
    # can initialize values when a new class instance created
    self.data = 0
    self.array = []
    self.name = name  # can store passed attributes

  # method --> function inside a class
  def bark(self):
    print("bark")

  def set_age(self, age):
    self.age = age

# to make an instance of a class or object call its constructor
# d = Dog("hello")


class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
  
  def get_grade(self):
    return self.grade


class Course:
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students
    self.students = []

    # convention to make private fields start with underscore
    self._secret = "string"  # still accessible outside class
  
  def add_student(self, student):
    if len(self.students) < self.max_students:
      self.students.append(student)
      return True
    return False

  def get_average_grade(self):
    total_points = 0
    for student in self.students:
      total_points += student.get_grade()
    
    return total_points // len(self.students)

c = Course("name", 12)
