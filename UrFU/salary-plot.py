import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("salary.csv", sep=";", encoding="cp866")

data = data.drop(0, axis=0)

colheads = list(data.loc[1])
#print(colheads)

cols = []
for i in range(26):
    cols.append(chr(ord('A')+i))
#print(cols)

header = {}
for i in range(len(cols)):
    header[cols[i]]=colheads[i]
print(header)

data.columns = cols

data = data.drop(1, axis=0)
data = data.drop([2148,2149,2150], axis = 0)

staffs = list(set(data['E']))
staff_out = []
for s in staffs:
    if '\n' in s or '#' in s or 'Ст' in s or 'спорт' in s:
        staff_out.append(s)

for s in staff_out:
    ind = data[data['E'] == s].index
    data = data.drop(ind, axis = 0)
    
data = data.astype({'E': float})
for i in list(data.columns)[7:]:
    data = data.astype({i: float})

ind = list("ACFGJKMNOPQRSTUWXY")
data = data.drop(ind, axis = 1)

data1 = data.groupby('B').sum()
data1 = data1.sort_values('Z', ascending = True)

ind = data1[data1['Z'] == 0].index
data1 = data1.drop(ind, axis = 0)

data1['N'] = np.arange(1,len(data1)+1)/len(data1)
data1['Zcs'] = data1['Z'].cumsum()/data1['Z'].sum()

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(8,6))
sc = sns.scatterplot(data = data1, x = 'N', y = 'Zcs', size = 'E', hue='H', ax = axes[1])

p1 = sns.lineplot(data = data1, x = 'N', y='Z', ax  = axes[0])