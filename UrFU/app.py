class Person():
    def __init__(self, n):
        self.name = n

class Employee(Person):
    def __init__(self,n):
        super().__init__(n)
    
    def __str__(self):
        s = "Name:\t%s\nSalary:\t%i\n" % (self.name, self.__salo)
        return s

    @property
    def salary(self):
        res = self.__salo
        if self.name == "Baba Valya":
            res = "А вы с какой целью интересуетесь?.."
            
        return res
    
    @salary.setter
    def salary(self, n):
        self.__salo = n
    
    
baba = Employee("Baba Valya")
ivan = Employee("Ivan Doberman")

baba.salary = 120000
ivan.salary = 12000

print(baba)
print(ivan)

print(baba.salary)
print(ivan.salary)
#print(baba.__salo)
        
