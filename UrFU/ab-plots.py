import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data_fake.csv", sep=";", encoding="cp1251")
print(data.info())

df_dt = pd.to_datetime(data['Дата создания']).dt.strftime('%y-%m-%d %H').str.split(" ", expand = True)
df_dt.columns = ['Date', "Hour"]
data = pd.concat([data, df_dt], axis = 1)

data_TS = data.groupby('Date')['ЛД'].count()

h = data.pivot_table(index="Hour", columns="Date", values='ЛД', aggfunc='count')

d = data.groupby('Образовательный уровень')['№'].count()

#plt.plot(data_TS.cumsum())

#fig = plt.figure(figsize=(8,6))
#lp = plt.plot(data_TS)
#plt.title("Динамика подачи заявлений", fontsize = 20)
#plt.xlabel("Дата")
#plt.ylabel("Количество личных дел")

#ndata = np.random.standard_normal(1000)
#fig = plt.figure(figsize=(8,6))
#n = sns.histplot(data=ndata, bins = 7, kde=True)

#fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (8,6))
#plt.suptitle("Динамика подачи заявлений", color = 'blue', fontsize = 20, weight = 'bold')
#plt.figtext(0.2, 0, "Рис. 1.1. Ход подачи заявлений")
#plt.subplot(122)
#p1 = plt.plot(data_TS.cumsum(),"*-")
#plt.title("Динамика числа \nподанных заявлений", color='green', weight = 'bold', fontsize=12)

#plt.subplot(121)
#p2 = plt.hist(data_TS, bins = 7, density = True)
#plt.title("Распределение числа \nподанных заявлений", color='green', weight = 'bold', fontsize=12)

#p1 = sns.lineplot(data=data_TS.cumsum(), ax = axes[0])
#p3 = sns.lineplot(data=data_TS, ax = axes[0])
#p1.set_title("Динамика числа \nподанных заявлений", color='green', weight = 'bold', fontsize=12)
#p1.set_xlabel('Дата')
#p1.set_ylabel('Количество заявлений')

#p2 = sns.histplot(data=data_TS, kde = True)
#p2.set_title("Распределение числа \nподанных заявлений", color='green', weight = 'bold', fontsize=12)
#p2.set_xlabel("Количество заявлений")
#p2.set_ylabel("Частота")

fig = plt.figure(figsize=(8,6))
#pie = plt.pie(d, labels=d.index, autopct = '%1.1f%%', startangle=60)
hmp = sns.heatmap(h)

plt.show()

