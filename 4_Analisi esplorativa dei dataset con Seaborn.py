import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mlp
import matplotlib.pyplot as plt

# usa plt.show() per visualizzare il grafico

import os
os.chdir("C:\\Users\\micci\\Documents\\Corso python data science\\CODICE - Corso completo di data science in Python\\Sezione 4")

churnm = pd.read_csv("churn_miss")

# https://seaborn.pydata.org/index.html

# Visualizzare grafico di una variabile qualitativa
sns.countplot(x = "gender", data = churnm) #conta i casi per variabile

sns.barplot(x = 'gender', y = 'lasttrans', data = churnm, palette = "rainbow") # due variabili
sns.boxplot(churnm['age']) # solo su variabili numeriche
sns.kdeplot(churnm.age) # andamento di una singola variabile
sns.violinplot(churnm['age'], palette='Set2') # violino
sns.stripplot(x = "label", y = "age", data = churnm, jitter = True) # scatter plot
sns.stripplot(x = "label", y = "age", data = churnm, hue = "gender", jitter = True) # posso aggiungere per es. la discriminante per sesso (posso anche agg "split = True" per dividere le colonne)
sns.jointplot(x = 'age',y = 'lasttrans', data = churnm, kind = 'scatter') # altro tipo di scatter
sns.jointplot(x = 'age',y = 'lasttrans', data = churnm, kind = 'hex')

# Dati relativi ad un analisi di regressione

sns.lmplot(x = 'lasttrans', y = 'age', data = churnm)
sns.heatmap(churnm.isnull(), yticklabels = False) # per vedere i casi mancanti

sns.set_style("white") # temi che possiamo mettere nei nostri grafici


# utilizziamo il dataset iris, incluso in seaborn
iris = sns.load_dataset('iris')
sns.pairplot(iris) # grafico delle variabili
