# 00. FUNCTIONS

file = open('file_name.txt', "r")
for line in file:
  print(line)
file.close()  # close file to release resources

f = open("new_file", "w")
f.write("Hello world")
f.close() 


# 01. WITH METHOD (BEST PRACTICE) - automatically closes file using a context manager
# often used with file systems to ensure file is closed after use
# context manager runs a enter and exit protocal betore/after block of code

# open function returns a file object and AS keyword assigns it a variable
# with ensures proper closing even if exception
with open('file_name.txt', "r") as f:
  for line in f:
    print(line)


# 02. try except block
try:
  with open("does_not_exist", "r") as f:
    pass
except Exception as e:
  print(e)
finally:
  print("test done")


"""
file modes:
  a append
  w write
  r read
"""