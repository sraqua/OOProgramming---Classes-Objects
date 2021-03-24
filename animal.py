class Animal:
  # __init__ = initialise 
  def __init__(self,name,age): 
  #  instance variable
  # each instance variable begins with self.
    self.name = name   
    self.age = age
  
  # instance method
  def speak(self):
    return f"My name is {self.name} and I am {self.age} years old"