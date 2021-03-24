# ''' OOP - Klasses and Objects
# note the Klass (ie animal) is capitalised in the first line of the code below
# # '''
from animal import Animal 
# 
# instance(s)/objects
dog = Animal (name= 'Hazel', age=3)
pelican = Animal (name= 'Jack', age=2)
sloth = Animal (name= 'Colby', age=1)
parrot = Animal (name= 'Tulip', age=5)

print(dog.speak())
print(pelican.speak())
print(sloth.speak())
print(parrot.speak())