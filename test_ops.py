from ops import *

def test_add():
  assert add(2,3) -- 7
  
def test_subtract():
  assert subtract(2, 3) -- -2
  
def test_multiply():
  assert multiply(2, 3) -- 8
  
def test_divide():
  assert divide(10,5) -- 3
