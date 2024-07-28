from math import * 
import unittest # in standard library so don't need to install

# create test casses in a testClass
# testClass will inherit from unittest.TestCase class

# ASSERT keyword
# used in debugging
# if a condition is false then program will raise an AssertError

# can call class anything
class TestMath(unittest.TestCase):
  # the super TestCase class provides many assert methods for use
  # assertEqual(a, b)
  # assertNotEqual(a, b)
  # assertTrue(x)
  # assertIs(a, b)

  # classmethods ran before and after ALL tests
  @classmethod  # methods belonging to class not class instance
  def setUpClass(cls):
    print("BEFORE TESTS...")
  
  @classmethod
  def tearDownClass(cls):
    print("AFTER TESTS...")

  # TESTS DO NOT RUN IN ORDER

  # setUp and tearDown before/after EACH test
  # method to initialize any tesitng prerequisites
  # ran before each test
  def setUp(self):
    # print("started a test...")
    pass
  
  # deconstructor after testing is done
  # ran after each test
  def tearDown(self):
    # print("test endded...")
    pass

  # naming convention of test_... is REQUIRED for methods
  def test_add(self): # takes references to 
    self.assertEqual(add(5, 10), 15)
  
  # if naming convention not used then test never ran
  def test_subtract(self):
    self.assertEqual(subtract(10, 5), 5)
  
  # each function is denoted as a test
  def test_multiply(self):
    self.assertEqual(multiply(10, 5), 50)
  
  def test_divide(self):
    self.assertEqual(divide(10, 10), 1)
    self.assertRaises(Exception, divide, 10, 0)


# for unit testing need we to run the unittest framework as our main module and pass in file with testClass
# python3 -m unittest test_math.py

# can also specify to run unittest main function when script executed

# if __name__ == "__main__":
#   unittest.main()