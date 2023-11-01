from ops import *

def test_add():
  assert add(2,3) == 5, 'error in addition'
  
def test_subtract():
  assert subtract(2, 3) == -1, 'error in subtraction'
  
def test_multiply():
  assert multiply(2, 3) == 6, 'error in multiplication'
  
def test_divide():
  assert divide(10,5) == 2, 'error in division'
