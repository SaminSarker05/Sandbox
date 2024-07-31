class Employee:
  g = 9.81

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last 
    self.pay = pay 

  # special methods for classes that specify interactions 
  def __repr__(self):
    pass  # used for debuging and logging
  
  def __str__(self):
    # used whenever a class instance is printed
    return self.first
  
  # can specify behavior for adding
  def __add__(self, other):
    return self.pay + other.pay 

  # MANY OTHERS --> called dunder methods for 2 underscores
  """
  __sub__
  __mul__
  __mod__
  __and__
  __xor__
  __len__
  """
  
c1 = Employee("samin", "sarker", 400000)
print(c1)
c2 = Employee("samin", "sarker", 800000)
print(c1 + c2)

