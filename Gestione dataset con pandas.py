## Importare un dataset

import pandas as pd # cosi che ogni volta che chiamiamo una funzione di pandas scriveremo pd

import os
os.chdir("C:\\Users\\micci\\Documents\\Corso python data science\\CODICE - Corso completo di data science in Python\\Sezione 4")

df1 = pd.read_csv("df.csv")
print(df1)

# Manipolazione dataFrame 
df1 = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis', 'Laura', 'Mary', 'Julian', 'Rosie', 'Simon', 'Laura'],
                   'Height':[180, 165, 170, 164, 163, 175, 166, 180, 164],
                   'Weight':[85, 65, 68, 45, 43, 72, 46, 85, 45],
                   'Pref_food': ['steak', 'pizza', 'pasta', 'pizza', 'vegetables', 'steak', 'seafood', 'steak', 'pizza'],
                   'Sex': ['m','f','m','f','f','m','f', 'm', 'f']})

# Piccola analisi esplorativa del df
df1.describe()




