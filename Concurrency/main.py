import threading 
import time 

# join commands ensure thread has finished running before continuing

ls = []

def call():
  for i in range(1, 11):
    ls.append(i)
    time.sleep(0.5)

x = threading.Thread(target=call, args=())
x.start()

print('script thread sending operation...')
x.join()  # won't go past this line until thread has stopped

print(ls)

def count(n):
  for i in range(1, n + 1):
    print(i)
    time.sleep(0.01)

# starts two more threads
for _ in range(2):
  x = threading.Thread(target=count, args=(10, ))
  x.start()


# def func():
#   print('ran')
#   time.sleep(10)
#   print('done')

# # to make a thread need to make a function that acts as operation
# # create a Thread object from the threading library
# # arguments
#   #   - target = function to be thread
#   #   - args = tuple of arguments for function if needed
# x = threading.Thread(target=func, args=())

# x.start() # starts thread

# # script itself is a thread
# # if we start a thread we now have two threads
# print(threading.active_count())  # print active threads

# # func function will hang because of time.sleep
# # when hanging, the core will switch to our script thread and execute the print statement
