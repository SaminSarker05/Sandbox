# python has support for type hints, annotation
# ignored at runtime but useful for ide's
# python compilation generates bytecode stored in __pycache__ as .pyc files


def myfunction(parameter: int) -> str:
  return "hello world" + parameter

def otherfunction(other: str):
  return other 

def another(scalar: float, servers: list[int]) -> None:
  print("hello world")


# can also do for variables
x: int = 1
x: float = 1.0


another(3.14, [1,23])

