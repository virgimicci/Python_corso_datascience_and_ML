# Machine Learning con Python

# Utilizza dati che gia abbiamo per predirre dati futuri
# Fasi del machine learning

# - PREPROCESSING (ripulire il dataset da eventuali problemi e se necessario standardizzarlo)
# - SCELTA DEL MODELLO (scelda di uno o piu algoritmi a seconda del tipo di problema e formulazione del modello
# di predizione. Dopo di che verrà estratto un oggetto detto di train e uno di test. Generalmente l'oggetto
# di train contiene il 70/80 % dei casi mentre quello di test il restante 20/30 %. Il modello viene creato
# sull'oggetto di train che puo poi essere applicato sull'oggetto di test. 
# Quanto il modello prevede abbastanza bene sull'oggetto di test si puo mettere alla prova
# su un dataset con dei dati non etichettatti (sup); sudataset nonsup non abbiamo una variabile etichetta quindi usiamo
# techiche di clustering)


# Tipi di algoritmi (modelli di data mining):

# - Supervisionati
#     - Classificazione (knn, Naive Bayes, Alberi di decisione)
#     - Regressione (modelli lineari, SVM)
# - Non Supervisionati
#     - Clustering (K-means)
#     - Regole di associazione
# - Semi-supervisionati
#    - Modelli graph-based
#     - Modelli generativi
# - Attivi


### MODELLI SUPERVISIONATI ####
# dataset etichettati, ovvero la variabile contiene il dato che poi vogliamo predire
# questo dataset è di *training* che permette poi di estrarre un modello che sara capace di 
# assegnare le classificazione ad un dataset senza le etichette

## Analisi di Regressione ##

# legame di una variabile dipendente ad una indipendente 
# esistono tantissime tecniche di regressione (lineare, lin multipla, multivariata
# non lineare, logistica etc...)

### REGRESSIONE LINEARE SEMPLICE y = B0 + B1X + Ɛ

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# stud= titolo di studio (indipendente), red= reddito (dipendente)
df = pd.DataFrame({'stud': [1,2,3,4,5,6,4,1,2,1,3],
                   'red':[12000,23000,35000,47000,55000,67000,43000,15000, 25000,15000,31500]})

plt.plot(df['stud'], df['red'],"ro")

# trasformiamo il df in matrice
mat = np.matrix(df)

x = mat[:,1] # salvo la variabile indipendente come x
y = mat[:,0] # salvo la variabile dipendente come y

# importiamo il modello che ci serve dal pacchetto sklearn (scikit learn)
# conda install -c conda-forge scikit-learn
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(y, x) # adattiamo il modello ai dati

# stampiamo intercetta e coeffciente
lr.intercept_
lr.coef_

# per es predizione di stipendio di qualcuno che ha il titolo di studio 4 (laurea)
lr.predict(4)


### REGRESSIONE LINEARE MULTIPLA
# piu variabili numeriche

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importiamo ora i dati
from sklearn.datasets import load_boston # importiamo il dataset presente su sklearn
boston = load_boston()

# ispezioniamo i nostri dati
type(boston)
# sklearn.utils.Bunch

boston.data.shape
# (506, 13) # 506 casi e 13 variabili 

print(boston.DESCR) # per descrizione dati

# possiamo utilizzare le funzionalità del pacchetto pandas per creare un dataframe "classico"
boston2 = pd.DataFrame(boston.data)

boston2.columns = boston.feature_names # agg i nomi alle colonne

# creiamo un df con i prezzi
price = boston.target
plt.hist(price, bins='auto')
#label
plt.xlabel('Prezzo delle case')
plt.ylabel('Numero di case')
plt.show()

# il nostro scopo è predire il costo di una casa n di cui conosciamo i dati ma non il prezzo
# concateniamo in un unico df

price2 = pd.DataFrame(price)
df = pd.concat([boston2, price2], axis = 1)
df.shape # (506, 14)

df = df.rename(columns = {0: 'price'}) # rinominiamo l'ultima colonna

# importiamo il modulo di regressione da scikit-learn

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

# importiamo il modulo che ci serve per creare un oggetto di train e uno di test
from sklearn.model_selection import train_test_split

# creiamo modello predittivo utilizzando il train e poi il modello lo applichiamo sugli elementi contenuti nel test
# funzione train_test_split per dividere il df in 4 parti: variabile etichetta contenuta solo in y
# test size: perc di casi che antranno nel dataset, solitamnete 20/30 %
x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, :13], df['price'], test_size = 0.3)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (354, 13) (152, 13) (354,) (152,)

# creiamo il modello di regressione utilizzando ovvetto di train e lasua etichetta (y_train)
lr.fit(x_train, y_train)

# a questo punto dobbiamo predirre i risultati ottenuti sull oggetto di test
pred = lr.predict(x_test)
plt.scatter(y_test, pred)

r2 = r2_score(y_test, pred)
r2 # 0.7248009333371008

### REGRESSIONE LOGISTICA
# Ha solo 2 tipi di clssificazione, ossia 0 e 1 (esempio per testi)

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('pid.csv')



