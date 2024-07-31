# can create unit tests using unitttest python module
# unit tests --> testing of isolated code components for expected behavior

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y 

def multiply(x, y):
  return x * y 

def divide(x, y):
  if y == 0:
    # use raise keyword to throw an exception
    raise Exception("division by 0")
    # can also use built in exceptions
    # raise ValueError("division by 0")
  return x / y 

# only run the lines in this file if this script is our mian module
if __name__ == "__main__":
  pass