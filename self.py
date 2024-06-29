class Dog:
    
    def __init__(self, name, age): # it will be applied when the Dog() object is called by default
        self.name = name #created an attribute of class dog which is name
        #Stored parmenently and can be called anytime
        print(name)
        
        self.age = age
        
    
    def get_name(self):
        return self.name
    
    def get_age(self): #use those init self attributes
        return self.age
    
    def set_age(self, age): #modify the self attributes
        self.age = age
        
        
d = Dog("Timmy", 34) #defined d as class dog
d2 = Dog("Billy", 12)

print(d.name)
print(d2.get_name())

print(d2.get_age())

d2.set_age(23)

print(d2.get_age())