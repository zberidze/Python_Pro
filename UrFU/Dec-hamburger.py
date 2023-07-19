def bread(func):
    def wrapper(arg):
        bread = [" "*8+"Хлеб"*4,"    "+"Хлеб"*7,"Хлеб"*9]
        print()
        print(bread[0])
        print(bread[1])
        print(bread[2])
        print()
        
        func(arg)
        
        print(bread[2])
        print(bread[1])
        print(bread[0])
        print()
        
    return wrapper

def inner(func):
    def wrapper(arg):
        cheese = "Сыр"*12
        salad = "Зелень"*6
        
        print (cheese)
        print()
        
        func(arg)
        
        print(salad)
        print()
    return wrapper

@bread
@inner
#@bread
def hamburger(meat):
    print("  "+meat*4)
    print("  "+meat*4)
    print()

meat = "Говядина"
hamburger(meat)
meat = "Цыпленок"
hamburger(meat)
