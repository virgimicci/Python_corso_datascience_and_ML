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

# Regressione lineare semplice y = B0 + B1X + Ɛ
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# stud= titolo di studio (indipendente), red= reddito (dipendente)
df = pd.DataFrame({'stud': [1,2,3,4,5,6,4,1,2,1,3],
                   'red':[12000,23000,35000,47000,55000,67000,43000,15000, 25000,15000,31500]})

plt.plot(df['stud'], df['red'],"ro")
