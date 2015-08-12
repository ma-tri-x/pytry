class Person:
  def __init__(self,name):
    self.namex = name
  def say_hi(self):
    print 'Hello, my name is', self.namex
    
    
p = Person('Max')
p.say_hi()
# The previous 2 lines can also