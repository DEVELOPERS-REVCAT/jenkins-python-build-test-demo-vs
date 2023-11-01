from ops import *

def test_add():
  assert add(2,3) == 7, 'error in addition'
  
def test_subtract():
  assert subtract(2, 3) == 2, 'error in subtraction'
  
def test_multiply():
  assert multiply(2, 3) == 8, 'error in multiplication'
  
def test_divide():
  assert divide(10,5) == 3, 'error in division'
