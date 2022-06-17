import os
os.chdir("C:\\Users\\micci\\Documents\\DATASETS to train")
import pandas as pd

mushrooms_db = pd.read_csv("mushrooms.csv") # FROM (https://archive.ics.uci.edu/ml/datasets/Mushroom)

# Esploriamo un po il dataframe

# The .describe() method will gives you the statistics of the columns
mushrooms_db.describe()

# display basic info about data type
mushrooms_db.info()

# Using value_counts() method we can see that the dataset is balanced
mushrooms_db['cap-color'].value_counts()
mushrooms_db['odor'].value_counts()

# Check for null values
mushrooms_db.isnull().sum()

# Manipolazione dati
