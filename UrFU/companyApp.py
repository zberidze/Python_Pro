from companyClass import Person, Employee
import pickle

ivan = Employee("Ivan Doberman", 24, "Boss", 12000)
stepan = Employee("Stepan", 23, "Underboss", 6000)
babavalya = Employee("Baba Valya", 84, "Big Boss", 120000)

company = [ivan, stepan, babavalya]

babavalya.salary = 160000

print("Before Export\n")
for i in company:
    print(i)

print("Exporting...\n")    
try:
    dumpfile = open("comp.db", "wb")
    res = pickle.dump(company, dumpfile)    
except:
    print("ERROR!\n")
else:
    print("DONE!\n")
finally:
    dumpfile.close()

print("After Export\n")
for i in company:
    print(i)

print(Person.__str__(babavalya))
print(Employee.__str__(babavalya))


    