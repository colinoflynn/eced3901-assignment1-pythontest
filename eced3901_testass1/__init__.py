import random
class TestStudentCode(object):
  """
  This class will test a simple student code class called StudentCode.

  The class must provide:

  1) In the initilization function, which saves two internal constants constants:
    A = the last digit of your banner number (int)
    B = the second to last digit of your banner number (int)
  2) The `banner_number` attribute (string), which will be defined in the
    __init__() function
  3) A function called `int_banner()` which takes no arguments and
     returns an integer (not string) showing the integer value of the
     last 6 digits of the banner number (e.g., after B00).
  4) A function called `add_b_const()` which adds the B constant (defined above)
     to the passed argument. The passed argument may be a string representation
     of an integer. If the passed string is invalid it must raise TypeError .
  5) A function called `add_a_or_b_const()` which has this call type:
      `def add_a_or_b_const(x, a_or_b="a"):`
        And behaves as follows:
          If called with just a number, like add_a_or_b(1) it adds "A" constant.
          If called with "a" or "b" specified, it adds that constant instead
          If called with any other value for `a_or_b` it raises ValueError
  """


  def OpenCode(self):
    self.sc = StudentCode()
    print("Checking for init attributes:")
    try:
      bn = self.sc.banner_number
    except AttributeError:
      print("FAIL: No 'banner_number' attribute, define with 'self.banner_number' in init function")
      raise IOError("Student tests failed")

    if bn.capitalize()[0:3] != "B00":
      print("FAIL: Banner number needs to start with 'B00'")
      raise IOError("Student tests failed")
    
    self.aconst = int(bn[-1])
    self.bconst = int(bn[-2])
    self.bannerint = int(bn[2:])
    print(" [OK], using %d as A and %d as B. Using %d as bannerint." % (self.aconst, self.bconst, self.bannerint))

  def Test1(self):
    print("Checking for banner conversion function & correctness")
    try:
      if self.sc.int_banner() != self.bannerint:
        print("FAIL: Expected %d, got %d"%(self.bannerint, self.sc.int_banner()))
    except AttributeError:
      print("FAIL: No 'int_banner' function, define with 'def int_banner(self):'")
      raise IOError("Student tests failed")

    print(" [OK]")

  def Test2(self):
    print("Checking for 1 argument input function & correctness (AttributeError means no function defined!)")
    rnd = random.randint(0, 100)
    c = self.sc.add_b_const(rnd)
    if c is None:
      print("FAIL: No return value from add_b_const")
      raise IOError("Student tests failed")
    if c != self.bconst + rnd:
      print("FAIL: Expected %d, got %d"%(self.bconst + rnd, c))
      raise IOError("Student tests failed")
    print(" [OK]")

    print("Checking student handled conversion of input types to int when possible")  
    rnd = random.randint(0, 100)
    c = self.sc.add_b_const(str(rnd))
    if c != self.bconst + rnd:
      print("FAIL: Expected %d, got %d"%(self.bconst + rnd, c))
      raise IOError("Student tests failed")
    print(" [OK]")

    print("Checking student handled raising of InputError exception")
    rnd = random.randint(0, 100)
    try:
      c = self.sc.add_b_const(str(rnd) + " " + str(rnd))
    except ValueError:
      print("FAIL: Function raises ValueError, spec requires TypeError")
      raise IOError("Student tests failed")
    except TypeError:
      print(" [OK]")    
    else:
      print("FAIL: Function supresses exceptions")
      raise IOError("Student tests failed")

  def Test3(self):
    print("Checking for 2 argument input function & correctness (AttributeError means no function defined!)")
    rnd = random.randint(0, 100)
    c = self.sc.add_a_or_b_const(rnd)
    if c is None:
      print("FAIL: No return value from add_a_or_b_const")
      raise IOError("Student tests failed")
    if c != self.aconst + rnd:
      print("FAIL: Expected %d, got %d"%(self.aconst + rnd, c))
      raise IOError("Student tests failed")

    c = self.sc.add_a_or_b_const(rnd, a_or_b="b")
    if c is None:
      print("FAIL: No return value from add_a_or_b_const")
      raise IOError("Student tests failed")
    if c != self.bconst + rnd:
      print("FAIL: Expected %d, got %d"%(self.bconst + rnd, c))
      raise IOError("Student tests failed")   

    try:
      self.sc.add_a_or_b_const(rnd, a_or_b="c")
    except ValueError:
      print(" [OK]")    
    else:
      print("FAIL: Function does not raise ValueError for invalid a_or_b")
      raise IOError("Student tests failed")
  
  def test_student_code(self):
    try:
      self.OpenCode()
      self.Test1()
      self.Test2()
      self.Test3()
    except IOError:
      print("Student tests failed")
      return
    print("**********All tests passed!***********")
    print("Check B00 number matches (%s)"%self.sc.banner_number)  
