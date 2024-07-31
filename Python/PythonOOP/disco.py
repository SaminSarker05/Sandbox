# object is an instance of a class
# objects have attributes and methods
# classes can also have attributes and methods (classmethods)

from car import Car 
# importing Car class from car module/python file

# self --> reference to object instance automatically passed in
car1 = Car("bmw", "s1", 2024, "blue")
car1.drive()

# DISTINCTION BETWEEN CLASS AND OBECT ATTRIBUTES/METHODS
# cls -> reference to a classes methods/attributes
# self -> reference to class instance/object methods/attributes

print(car1.get_numbers())
Car.print_hello()

# STATIC VS CLASS METHODS
# staticmethod -> cannot modify or access class state (utility)
# classmethod -> can modify or access class state