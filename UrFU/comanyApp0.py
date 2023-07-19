import pickle
from companyClass import Person, Employee

try:
    dumpfile = open("comp.db", "rb")
    company = pickle.load(dumpfile)
    
    for i in company:
        print(i)

except: 
    print("ERROR!\n")
else:
    print("DONE!\n")
finally: 
    try: 
        dumpfile.close()
    except:
        pass

print("ADIOS!\n")

