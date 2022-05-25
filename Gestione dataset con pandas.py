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

# Ordinare un data set in base ad una variabile numerica

df.sort_values(by= "Weight")

# estrarre dei case dal data set (slicing)
df1(2:) # dal secondo in poi

# metodi per slicing .loc (lavora in base all'indice) 
df1.loc[1]

# .iloc (estrae in base alla posizione) 
df1.iloc[1, 4]

# e .ix (estrae in base alla posizione e indice) 
df1.ix[1:3, :4]

# condizioni di estrazione
df1[df1.Height > 170]
df1[df1['Sex'] == "m"]

g1 = df1.groupby('Sex')
g1.groups

g1.describe() # ottengo info relative ai gruppi creati

df1.join() # per unire un altro df al nostro

del df1["new_col"] # per elimianre una colonna

df1.T() # inverte righe e colonne
df1.sample(3) # estrae casualmente tre casi dal df

# se voglio sempre gli stessi casi bisogna impostare un seed, con il pacchetto numpy
import numpy as np

np.random.seed(1) # numero qualunque
df1.sample(2) # se ripeto l'operazione, ridefinendo lo stesso seed, ottengio gli stessi campioni

## Numpy permette di creare dataset casuali 
# oltretutto ci permette di ottenere altri tipi di distribuzione
# binomiale

pd.DataFrame(np.random.binomial(100, 0.5, (10, 5)))

# poisson
pd.DataFrame(np.random.poisson(100, (10, 5)))

# uniforme
pd.DataFrame(np.random.uniform(1, 100,  (10, 5)))


## Matplotlib : pacchetto per la creazione di grafici (gia presente in anaconda) 
# (https://matplotlib.org/)

import matplotlib as mlp
import matplotlib.pyplot as plt

#funzione base .plot

plt.plot([5,7,2,4]) # grafico con linea di defoult
plt.plot([5,7,2,4], [4,6,9,2], 'ro') # ro (round obj) inserisce pallini e non linea

# creiamo due liste

x = [50, 70, 90, 65]
y = [129, 192, 163, 172]

plt.plot(x, y, linewidth = 1.0, ls = '-' #linestyle
         , marker = "o" # scelgo il marker dei dati sulla linea
         , markersize = 10, markerfacecolor = 'white') # personalizzazione

help(plt.plot) # per visualizzare la documentazione relativa alla funzione

# personalizzazione grafico
plt.plot(x, y, color = "yellow")
plt.title("TITLE", color = "blue")
plt.xlabel("Asse X", color = "purple")
plt.ylabel("Asse Y", color = "green")
plt.grid(True) # se voglio la griglia sotto
plt.legend(["Legend"], loc= 2) # per aggiungere la legenda, "loc" serve per la posizione

plt.subplot[2,2,1] # sottografici, i num tra parentesi indicano numero di righe, di colonne e num del grafico
plt.plot([1,2,3,4],[12,4,15,6],"a")
plt.subplot[2,2,2] # sottografici
plt.plot([1,3,6,9],[11,9,19,3],"b")

# altri grafici
plt.pie()
plt.scatter()
plt.bar()
plt.barh()
plt.area()
plt.hist()
plt.boxplot()
# posso anche scrivere df1.plot(kind = "hist")

plt.savefig("graph1.png", dpi= 600) # per salvare l'immagine nella wd

# Applicare uno stile
#stili disponibili
plt.style.available

# come applicarli?
plt.style.use("ggplot")
df1.plot(kind = "area")








