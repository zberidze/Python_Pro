import pandas as pd

data = pd.read_csv("data_fake.csv", sep=";", encoding="cp1251")
data.info()

data = data.drop(['Факультет',
       'Срок обучения', 'Курс',
       'Специальность',
       'Тип док. об обр.', 'Серия', 'Номер', 'Ср. балл', 'Награды',
       'Оригинал', 
       'Дата создания', 'Тех. секретарь', 'Unnamed: 27'],axis=1)

data.columns=['num', 'Case', 'Name', 'Stat', 'Prior', 'Rate',
                     'Form','Term', 'Code', 'Level',
       'Commis', 'Comm', 'Budg', 'General', 'Purp']


print("Deleting Purose Column")
ind = data[data['Purp'] == "да"].index
data = data.drop(ind, axis=0)
#print(data)
#print(data[data['Purp']=='да'])
data = data.drop(['Purp'], axis = 1)
#print(data)

print("Deleting Comission Column")
#print(set(data['Commis']))
ind = data[data['Commis'] != "Бакалавры/Специалисты"].index
data = data.drop(ind, axis=0)
#print(data)
#print(set(data['Commis']))
data = data.drop(['Commis'], axis = 1)
#print(data.columns)

#print("Checking Bak/Spec")
#cases = list(set(data['Case']))
#print("TOTAL Cases: ", len(cases))
#for i in cases:
#    level = data.loc[data[data['Case'] == i].index,'Level']
#    level_num = len(level)
#    unique_level_num = len(set(level))
#    if unique_level_num > 1:
#        print(level, level_num, unique_level_num)
    
print("Deleting Budget Column")
#print(set(data['Budg']))
ind = data[data['Budg'] != "да"].index
data = data.drop(ind, axis=0)
#print(set(data['Budg']))
data = data.drop(['Budg'], axis = 1)
#print(data.columns)    

print("Deleting Term Column")
#print(set(data['Term']))
data = data.drop(['Term'], axis = 1)
#print(data.columns)    

print("Cleaning Status Column")
#print(set(data['Stat']))
s1 = 'Отменено'
s2 = 'Аннулировано'
s3 = 'Допущено'
s4 = 'Отказ'
s5 = 'В приказ по квоте'

ind = data[
    (data['Stat'] == s1) |
    (data['Stat'] == s2) |
    (data['Stat'] == s3) |
    (data['Stat'] == s4) |
    (data['Stat'] == s5)
    ].index
data = data.drop(ind, axis=0)
#print(set(data['Stat']))

print("Deleting Comment Column")
#print(set(data['Comm']))

s1 = "Забрал документы"
s2 = "Отказался от участия в конкурсе"
s3 = "нет договора "

ind = data[
            (data['Comm'] == s1) |
            (data['Comm'] == s2) |
            (data['Comm'] == s3) 
          ].index
data = data.drop(ind, axis=0)
#print(set(data['Comm']))
data = data.drop(['Comm'], axis = 1)
#print(data.columns)   

print("Checkin Forms for Budgeting")
#print(set(data['Form']))
#b = data[(data['Form'] == 'очная')&(data['Stat'] == 'В приказ')]
#print(len(b))
#b = data[(data['Form'] == 'очно-заочная')&(data['Stat'] == 'В приказ')]
#print(len(b))
#b = data[(data['Form'] == 'заочная')&(data['Stat'] == 'В приказ')]
#print(len(b))

data.loc[data[data['Form'] == 'очная'].index, 'Form'] = 'O'
data.loc[data[data['Form'] == 'очно-заочная'].index, 'Form'] = 'OZ'
data.loc[data[data['Form'] == 'заочная'].index, 'Form'] = 'Z'

#print(set(data['Form']))
data['Spec']=data['Code']+data['Form']
specs = set(data['Spec'])
#print(specs)

budget = {}
for i in specs:
    b = len(data[(data['Spec'] == i)&
                 (data['Stat'] == "В приказ")])
    l = len(data[(data['Spec'] == i)&
                 (data['General'] == "нет")&
                 (data['Stat'] == "В приказ")])
    budget[i]=[b,l,b,l]
#print(budget)

bb = 0
for k in budget.keys():
    bb += budget[k][0]
print("TOTAL Budget: ",bb)

print("Cleaning Status")
data['Stat']=""

#print(list(set(data['Prior'])))
priorities = ['Первый', 'Второй', 'Третий', 'Четвертый']

for p in priorities:
    for s in specs:
        ls = data[
                (data['Prior'] == p) &
                (data['Spec'] == s) &
                (data['General'] == 'нет') &
                (data['Stat'] == "")
            ]
        ls_sort = ls.sort_values(by=['Rate'], ascending = False)
        
        if budget[s][3] < len(ls_sort):
            num = budget[s][3]
        else:
            num = len(ls_sort)
            
        for i in range(num):
            stud_num = ls_sort.iloc[i,0]
            data.loc[data[data['num'] == stud_num].index,
                     'Stat'] = 'В приказ'
        budget[s][3] -= num
        budget[s][2] -= num
        
        ss = data[
                (data['Prior'] == p) &
                (data['Spec'] == s) &
                (data['Stat'] == "")
            ]
        ss_sort = ss.sort_values(by=['Rate'], ascending = False)
        
        if budget[s][2] < len(ss_sort):
            num = budget[s][2]
        else:
            num = len(ss_sort)
            
        for i in range(num):
            stud_num = ss_sort.iloc[i,0]
            data.loc[data[data['num'] == stud_num].index,
                     'Stat'] = 'В приказ'
        budget[s][2] -= num
    
print(budget)
data.loc[data[data['Stat']==""].index, 'Stat'] = "Отклонено"

data.to_csv("out_data.csv", sep=";", encoding="cp1251")

#data.info()