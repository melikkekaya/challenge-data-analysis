"""Removing outliers and filling missing values in based on Multivariate Approach:
pip install scipy,  Scikit-learn, sklearn, run it after outliers are removed"""
from typing import List

import sklearn
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# Remove outliers
def remove_outliers(df: pd.DataFrame, columns: List[str], n_std: int) -> pd.DataFrame:
    for col in columns:
        mean = df[col].mean()
        sd = df[col].std()
        
        df = df[(df[col] <= mean+(n_std*sd))]
        
    return df

clean_houses = remove_outliers(df_houses, ['Price'], 3)
clean_apartments = remove_outliers(df_apartments, ['Price'], 3)

columns_h = ['Price','Living area','Number of rooms','Furnished','Garden','Terrace','Open fire','Surface of the land','Number of facades','Swimming pool','Building Cond. values','Kitchen values','Primary energy consumption', 'Energy efficiency']
columns_a = ['Price','Living area','Number of rooms','Furnished','Open fire','Building Cond. values','Kitchen values','Primary energy consumption', 'Energy efficiency']
impute_it = IterativeImputer()
np_array_houses = impute_it.fit_transform(clean_houses).astype(int)
np_array_apartments = impute_it.fit_transform(clean_apartments).astype(int)


complete_houses = pd.DataFrame(np_array_houses,columns = columns_h)
complete_apartments = pd.DataFrame(np_array_apartments, columns = columns_a)


