"""Removing outliers and filling missing values in based on Multivariate Approach:
pip install scipy,  Scikit-learn, sklearn, run it after outliers are removed"""

import pandas as pd
import urllib.parse
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from typing import List

import sklearn
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

#df for houses and apartments: 
df = pd.read_csv("clean_data.csv")
df_for_houses = df[df['Type of property'] == 'house']
df_for_apartments = df[df['Type of property'] == 'apartment']

columns_houses = ['Price','Living area','Number of rooms','Furnished','Garden','Garden surface','Terrace','Terrace surface','Open fire','Surface of the land','Number of facades','Swimming pool','Building Cond. values','Kitchen values','Primary energy consumption', 'Energy efficiency']
columns_apartments = ['Price','Living area','Number of rooms','Furnished','Garden', 'Garden surface', 'Terrace surface', 'Open fire','Building Cond. values','Kitchen values','Primary energy consumption', 'Energy efficiency']

df_houses = df_for_houses[columns_houses]
df_apartments = df_for_apartments[columns_apartments]

# Remove outliers
def remove_outliers(df: pd.DataFrame, columns: List[str], n_std: int) -> pd.DataFrame:
    for col in columns:
        mean = df[col].mean()
        sd = df[col].std()
        
        df = df[(df[col] <= mean+(n_std*sd))]
        
    return df

clean_houses = remove_outliers(df_houses, ['Price'], 3)
clean_apartments = remove_outliers(df_apartments, ['Price'], 3)

columns_h = columns_houses
columns_a = columns_apartments

impute_it = IterativeImputer()
np_array_houses = impute_it.fit_transform(clean_houses).astype(int)
np_array_apartments = impute_it.fit_transform(clean_apartments).astype(int)


complete_houses = pd.DataFrame(np_array_houses,columns = columns_h)
complete_apartments = pd.DataFrame(np_array_apartments, columns = columns_a)


