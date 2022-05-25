# 1. Data cleaning, GIGO
# - precisione (raccogliere o estrarre i dati)
# - completezza (in presenza di dati mancanti dobbiamo mettere in atto procedure di completamento o cancellazione)
# - dati duplicati (che vanno eliminati), outliers (non in linea con la nsotra distribuzione)

# 2. Dati mancanti
# - deletion (non considerare, ingorare o cancellare casi con dati mancanti)
# - imputation (sostituire dati mancanti con valori, fissi(es 0), misura di tendenza centrale (media/mediana) o imputazione probabilistica

# 3. Standardizzazione/normalizzazione


## COME GESTIRE I MISSING VALUES

import pandas as pd

df_missing = pd.read_csv("df_missing.csv")
print(df_missing)
#     A     B     C      D   E
# 0  15  96.0  74.0   31.0  50
# 1  41  27.0  74.0  279.0  57
# 2  21  32.0   NaN   99.0  96
# 3  48  97.0  50.0    NaN  69
# 4  63  98.0  74.0   44.0  55
# 5  43  11.0  80.0   74.0  33
# 6  39  38.0  81.0   20.0  41
# 7  58  31.0   NaN   76.0  91
# 8  85  94.0  37.0   65.0  60
# 9  98   NaN  19.0   43.0  32

df_missing.dropna() # cancelloi casi che abbiano almeno 1 missingvalue
df_missing.dropna(axis = 1, how = 'any') # cosi cancello le colonne che li hanno

df_missing.fillna(0) # imputiamo con lo 0 nei missing values
df_missing.fillna(df_missing.mean()) # imputiamo con la media

# imputazione con scikit-learn

from sklearn.preprocessing import Imputer # importiamo un modulo apposito
imp = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imp = imp.fit(df_missing.iloc[:, 1:4])
df_missing.iloc[:, 1:4] = imp.transform(df_missing.iloc[: , 1:4])

help(Imputer)


# Data cleaning, pulizia del dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students2.csv")
print(df)
#    ID  gender  subject  mark1  mark2  mark3       fres
# 0    1      mm        1   17.0   20.0   15.0        neg
# 1    2       f        2   24.0  330.0   23.0        pos
# 2    3  FEMale        1   17.0   16.0    NaN          0
# 3    4    male        3   27.0   23.0   21.0          1
# 4    5       m        2   30.0   22.0   24.0   positive
# 5    6       f        1   30.0   21.0   25.0          1
# 6    7       m        2   23.0   24.0   24.0          1
# 7    8       f        3   17.0    NaN   20.0          0
# 8    9      ma        1   21.0   24.0   24.0          1
# 9   10      ff        2   24.0   25.0   24.0        pos
# 10  11       f        2  224.0   22.0   25.0        pos
# 11  12       m        1   25.0   27.0   24.0          1
# 12  13       f        2   24.0   24.0   25.0          1
# 13  14       m        3    NaN   17.0   15.0        neg
# 14  15       m        2   22.0   27.0   24.0          1
# 15  16       f        1   30.0   24.0   27.0   positive
# 16  17     fem        2   29.0   27.0   23.0          1
# 17  18       m        3   29.0   26.0   22.0        pos
# 18  19       f        1    NaN   17.0   15.0   negative

# vediamo come le diciture sono diverse, presenza di NaN, outliers etc...

df.dtypes # per vedere che tipo di variabili abbiamo


df.replace([224], [24], inplace = True) # .replace per sostituire gli outliers, inplace= True non sovrascrive il df

# Solo dopo aver sistemato gli outlier lavoro sugli NaN, altrimenti se per es imputiamo
# con la media ci darebbero valori sballati

df['mark1'].fillna(df['mark1'].mean(), inplace = True)
df['mark2'].fillna(df['mark2'].mean(), inplace = True)
df['mark3'].fillna(df['mark3'].mean(), inplace = True)

# Ora voglio gestire le variabili qualitative
# iniziamo omogeneizzando i nomi su gender

# aggiungiamo una nuova col  chiamata gender_ricod

def ricodifica_gender(gender):
    if gender == 'm':
        return 0
    elif gender == 'male':
        return 0
    elif gender == 'mm':
        return 0
    elif gender == 'ma':
        return 0
    else:
        return 1
      
df['gender_ricod'] = df.gender.apply(ricodifica_gender)

# NORMALIZZAZIONE DEI DATI, trasformare tutti i dati in valori compresi in un range fisso
# - nomralizzazione min max
# - trasformazione in punti z

import pandas as pd
import numpy as np

# impostiamo il seed e creiamo il dataset

np.random.seed(12345)

df = pd.DataFrame(np.random.randint(200, size=(10, 6)))

# normalizzazione
# dal df sottraiamo il valore minimo e lo dividiamo per la differenza tra valore massimo e minimo
df_norm = (df - df.min()) / (df.max() - df.min()) # df in cui ogni valore è compreso tra o e 1

# importiamo il modulo per la standardizzazione
from sklearn import preprocessing

# standardizziamo
preprocessing.scale(df) # dataset in array

# possiamo procedere con lo scaling tramite scikit-learn:
df_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)) # qua gli diciamo che lo vogliamo tra 0 e 1
df_scaled = df_scaler.fit_transform(df) # viene sempre in array
df_scaled

import matplotlib as mlp
import matplotlib.pyplot as plt

df_norm.boxplot(return_type = "axes") # possiamo vedere gli outliers


# Codificare una variabile categorica in numerica
import pandas as pd

# creo df
df = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis', 'Laura', 'Mary', 'Julian', 'Rosie', 'Simon', 'Laura'],
                   'Height':[180, 165, 170, 164, 163, 175, 166, 180, 164],
                   'Weight':[85, 65, 68, 45, 43, 72, 46, 85, 45],
                   'Pref_food': ['steak', 'pizza', 'pasta', 'pizza', 'vegetables', 'steak', 'seafood', 'steak', 'pizza'],
                   'Sex': ['m','f','m','f','f','m','f', 'm', 'f']})

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# per esempio voglio codificare la variabile sex che è la numero 3
# con il metodo .iloc seleziono la variabile e la trasformo in numerica
df.iloc[:, 3] = LabelEncoder().fit_transform(df.iloc[:, 3]) 


# Creazione variabili dummy
# per utilizzare variabili qualitative all’interno di un modello di regressione
# costruire una variabile dummy significa infatti codificare i dati presenti 
# all’interno di una variabile in modo che possano assumere solo valore 0 oppure 1.

import pandas as pd

df = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis', 'Laura', 'Mary', 'Julian', 'Rosie', 'Simon', 'Laura'],
                   'Height':[180, 165, 170, 164, 163, 175, 166, 180, 164],
                   'Weight':[85, 65, 68, 45, 43, 72, 46, 85, 45],
                   'Pref_food': ['steak', 'pizza', 'pasta', 'pizza', 'vegetables', 'steak', 'seafood', 'steak', 'pizza'],
                   'Sex': ['m','f','m','f','f','m','f', 'm', 'f']})

df_dummy = pd.get_dummies(df['Sex'], prefix = 'Sex')
print(df_dummy)

#     Sex_f  Sex_m
# 0      0      1
# 1      1      0
# 2      0      1
# 3      1      0
# 4      1      0
# 5      0      1
# 6      1      0
# 7      0      1
# 8      1      0

df.join(df_dummy) # li inserisco nel df
