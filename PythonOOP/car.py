class Car:
  # class attribute
  numbers = 0

  # bound to class NOT the object
  @classmethod
  # receives implicit cls argument --> reference to cls
  def get_numbers(cls):
    return cls.numbers  # cls used to refer to class 
  
  # does not receive implicit cls argument
  # bound to class not object

  @staticmethod
  def print_hello():  # does not need cls reference
    print("hello world")


  def __init__(self, make, model, year, color):
    self.make = make
    self.model = model 
    self.year = year 
    self.color = color
    Car.numbers += 1
  
  def drive(self):
    print(f"{self.color} car is driving")
  
  def stop(self):
    print(f"{self.color} car is stopped")

# only run script lines if this file is our main module
if __name__ == "__main__":
  print("hello world")

# when we run a python file the __name__ special varialbe refers to python module being ran