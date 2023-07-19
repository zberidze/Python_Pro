class Person():
    counter = 0
    
    def __init__(self, n, a):
        Person.increment()
        self.number = Person.counter
        self.name = n
        self.age = a
    
    def __str__(self):
        s = "%i. My name is %s. I'm %i yars old.\n" % (self.number, self.name, self.age)
        return s
              
    @staticmethod
    def increment():
        Person.counter += 1
        
class Employee(Person):
    def __init__(self, n,a, p,s):
        super().__init__(n,a)
        self.pos = p
        self.salary = s
    
    def __str__(self):
        s = "My name is %s. \nI'm %s with %i-rubles salary!\n" % (self.name, self.pos, self.salary)
        return s