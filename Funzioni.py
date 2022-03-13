## Funzioni built-in, parte di py e vengono caricate in automatico
## Funzione user defined, che possiamo costruire
# utili per applicare una operazione su piu oggetti senza ripetere lo stessocodice piuvolte,
#permettono diiterare un operazione
## Funzioni presenti nelle librerie



## Come scrivere una funzione
# si compone di tre parti

 # def scopo_funzione"""nome"""(x): """parametri"""
 #   '''(x) -> y
 #   qui scriveremo la documentazione della funzione, quindi quello
 #   che la funzione esegue 
 #   '''
 #   return(x+y) '''body della funzione'''

# esempio

def moltiplica_xy(x,y):
    ''' voglio moltiplicare x e y
    '''
    return(x*y)

moltiplica_xy(4,6)

# Per rendere piucomplesse le funzioni possiamo utilizzare le istruzioni condizionali e i loops
# per gestire delle condizioni
# if, elif, else, for, while, continue e break

x = 5
y = 7

if x < y:
    print('x è minore di y')
else:
    print('y è minore di x')

''' x è minore di 7'''

# ciclo for; è un iteratore, in grado di percorrereuna sequenza e eseguire delle azioni

# for elemento in oggetto:
#     esegui azione su elemento


x = (1,4,7,34,8)

for n in x:
    print(n) # in questo caso quindi prende ogni elemento della tupla e la stampa

# ciclo while;  mette in esecuzione delle istruzioni se una data condizione è soddisfatta
x = 1
while x < 5:
    print(x)
    x = x + 1 # senza questa condizione partirebbe un loop infinito

# continue; salta un det elemento

l1 = [1,3,5,8,"gatto", 12,34,56] # volgio stampare gli elementi senza gatto

for item in l1:
    if item in l1:
        if item == "gatto":
            continue
        print(item)
        
        
## Funzione lambda
# riduce la funzione ad una sola riga, rende il codice piu snello

def square(x):
    return(x*x)

square(9)

sq2 = lambda x : x*x        

num = [2, 4, 7, 9]
list(map(sq2, num)

