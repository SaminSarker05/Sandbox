# FACTORY DESIGN PATTERN in python
# popular design pattern for classes to increase modularity; organization of seperate units

# like a factory each component can independently work

# interface defines what a class must have
# class defines how the object behaves

# abcmeata is a parent class used to create abstract classes; that can't be created
# serves as blueprint for other classes

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
  @abstractstaticmethod # method can be called without class instance
  def person_method():
    """ Interface method """


class Student(IPerson):
  def __init__(self):
    self.name = "hello world"

  # must override abstract methods
  def person_method(self):
    print("I am a person and student")


class Teacher(IPerson):
  def __init__(self):
    self.name = "teacher name"
  
  def person_method(self):
    print("I am a person and a teacher")


class PersonFactory:
  def build_person(person_type: str):
    if person_type == "student":
      return Student()
    if person_type == "teacher":
      return Teacher()
    
    print("invalid person type")
    return -1

  

def main():
  # won't work
  # p1 = IPerson()
  # p1.person_method()

  choice = input("what type of person do you want to build? ")
  person = PersonFactory.build_person(choice)
  if person != -1:
    person.person_method()


if __name__ == "__main__":
  main()
  print("running...")

