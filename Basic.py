# Python has a lot of class objects

print(type('Hello')) # A data stype class

def fun():
    return 0

print(type(fun))

#string is a class with method upper

name = 'abc'

print(name.upper())

"""

Let's make a class ourselves

"""

class Dog:
    
    # def __init__(self, name): # it will be applied when the Dog() object is called by default
    #     self.name = name
    
    def meow(self):
        return 'Meow'
    
    def addOne(self, x): #methods always have self first
        return x + 1
    
    def bark(self):
        print('Bark!!!!')
        
d = Dog() #defined d as class dog

print(type(d))

d.bark() #applied bark method on dog

print(d.addOne(5))