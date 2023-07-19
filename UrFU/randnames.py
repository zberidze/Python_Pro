import random

class Person():
    NAMES = ["Иван", "Петр", "Николай","Андрей", "Тимофей", "Сергей",
             "Дмитрий", "Алексей", "Владимир", "Борис", "Глеб",
             "Семен", "Степан", "Кондрат", "Игнат", "Иннокентий",
             "Трофим", "Терентий", "Кирилл", "Серафим", "Александр"]
    LNAMES = ["Баран", "Бык", "Ворон", "Медведь", "Лось", 
              "Плотник", "Столяр", "Конюх", "Кузнец", "Токарь", "Мельник", "Золотарь" ]
    FNAME_SFX = "ович"
    LNAME_SFX = ["ов", "овский", "енко", "ович"]
    BPLACE0 = ["с. ", "пос. ", "ПГТ "]
    BPLACE1 = ["Большие ", "Малые ", "Старые ", "Новые ", "Красные ", 
               "Южные ", "Северные ", "Ленинские ", "Дальние ", "Тощие "]
    BPLACE2 = ["Стыды", "Пипки", "Серпы", "Хутора", "Пикули", "Дали", "Рассветы",
               "Сады", "Зады", "Нюни", "Пруды", "Заветы"]
    
    def __init__(self):
        self.name, self.fname, self.lname = Person.randName()
        
        self.year = str(random.randint(1945, 2000))
        
        self.bplace = random.choice(Person.BPLACE0)+\
                      random.choice(Person.BPLACE1)+\
                      random.choice(Person.BPLACE2)
        
        self.snils = str(random.randint(100,999))+"-"+\
                     str(random.randint(100,999))+"-"+\
                     str(random.randint(100,999))+"-"+\
                     str(random.randint(10,99))
        
        inn = "" + str(random.randint(1,9))
        for i in range(11):
            inn += str(random.randint(0,9))
        self.inn = inn
    
    def __str__(self):
        s = self.name + " " + self.fname + " " + self.lname + " " + self.year + " г.р." + "\n" +\
            "уроженец " + self.bplace + '\n'+\
            "СНИЛС:\t" + self.snils+'\n'+\
            "ИНН:\t" + self.inn+'\n\n'
            
        return s
    
    def randName():
        # Случайно выберем имя
        rname = random.choice(Person.NAMES)
        
        # Случайно выберем имя и создадим отчество
        fname_prx = random.choice(Person.NAMES)
        if fname_prx[-1] == "й":
            rfname = fname_prx.rstrip('й') + 'e' + Person.FNAME_SFX[1:]
        else:
            rfname = fname_prx + Person.FNAME_SFX
        
        # Случайно выберем имя и созадаим фамилию
        r = random.randint(0,1) 
        
        if  r == True:
            lname_prx = random.choice(Person.NAMES)
            lname_sfx = random.choice(Person.LNAME_SFX)
            if lname_prx[-1] == "й":
                rlname = lname_prx.rstrip('й') + 'e' + lname_sfx[1:]
            else:
                rlname = lname_prx + lname_sfx
        else:
            lname_prx = random.choice(Person.LNAMES)
            lname_sfx = random.choice(Person.LNAME_SFX)
            if lname_prx[-1] == "ь":
                rlname = lname_prx[:-1] + 'e' + lname_sfx[1:]
            else:
                rlname = lname_prx + lname_sfx
                    
        return rname, rfname, rlname
    
class Student(Person):
    def __init__(self):
        super().__init__()
        UNIVS = ["UrFU", "MSU", "DONNTU"]
        self.univ = random.choice(UNIVS)
        
    def __str__(self):
        s = super().__str__()
        s += "Студент "+ self.univ + "\n"
        return s
        

def main():
    
    persons = []
    for i in range(100):
        persons.append(Person())
    
    persons[99].name = "John"
    persons[99].fname = '"Bastard"'
    persons[99].lname = "Snow"
    
    for i in persons:
        print(i)

    students = []
    for i in range(10):
        students.append(Student())
    
    for i in students:
        print(i)

main()