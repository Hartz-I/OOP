class Person:
    #varible without self is a class attribute
    #Class Attribute: attribue that applys on whole class including all instances
    total_person = 0
    
    def __init__(self,name,age,id,B_date):
        self.name = name
        self.age = age
        self.id = id
        self.B_date = B_date
        
        #using the class method everytime the class is defined
        Person.add_people_to_total()
        
    def profile(self):
        print(f"My name is {self.name}. I am {self.age} years old")
        
    def get_ID(self):
        print(self.id)
        
    #Class Method: method that applys on whole class including all instances
    @classmethod #decorator
    def add_people_to_total(cls):
        cls.total_person +=1
        
#defining a child class
class Maneger(Person):
    def __init__(self, name, age, id, B_date, supervision_count):
        super().__init__(name,age,id,B_date) #attributes of parent class
        
        #new attributes
        self.supervision_count = supervision_count
        self.position = 'Manager'
        self.salary = 15000
        self.activity = []
        self.employees = []
    
    #changed method based on child class
    def profile(self):
        print(f"My name is {self.name}. I am {self.age} years old. I am a {self.position} in this company.")
        print("People assigend under me are:")
        for employee in self.employees:
            print(employee)
        
    def set_salary(self, amount):
        self.salary = amount
    
    def add_activity(self, dictionary_entry):
        self.activity.append(dictionary_entry)
    
    def add_employee(self, employee):
        self.employees.append(employee.id)
        
        employee.get_assigned(self.id)
        
        
class Employee(Person):
    def __init__(self, name, age, id, B_date):
        super().__init__(name,age,id,B_date)
        self.position = 'Employee'
        self.salary = 10000
        self.penalty = []
        self.assigned_to = 'not assigned yet.'
    
    def add_penalty(self, dictionary_entry):
        self.penalty.append(dictionary_entry)
        
    def profile(self):
        print(f"My name is {self.name}. I am {self.age} years old. I am a {self.position} in this company. I am assigned to {self.assigned_to} id")
    
    def get_assigned(self, manager_id):
        self.assigned_to = manager_id
        
p = Person('Bob', '25', 12, 'June 21')
m = Maneger('Carl', '29', 1201, 'June 25',50)
e1 = Employee('Krillin', '19', 120101, 'Aug 7' )
e2 = Employee('Kril', '17', 120102, 'Aug 9' )

#before adding
print('Before Adding: ')
p.profile()
m.profile()
e1.profile()

m.add_employee(e1)
m.add_employee(e2)

#after adding
print("After Adding: ")
p.profile()
m.profile()
e1.profile()

print(Person.total_person)