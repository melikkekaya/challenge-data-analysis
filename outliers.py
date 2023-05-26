numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'bool']

df_houses = df[df['Type of property'] == 'house']
df_apartments = df[df['Type of property'] == 'apartment']
apartdf = df_apartments.select_dtypes(include=numerics)
housedf = df_houses.select_dtypes(include=numerics)



print(housedf['Price'].min())
print(housedf['Price'].max())

from typing import List
# Remove outliers
def remove_outliers(df: pd.DataFrame, columns: List[str], n_std: int) -> pd.DataFrame:
    for col in columns:
        print('Working on column: {}'.format(col))
        
        mean = df[col].mean()
        sd = df[col].std()
        
        df = df[(df[col] <= mean+(n_std*sd))]
        
    return df

new_housedf = remove_outliers(housedf, ['Price'], 3)

print(new_housedf['Price'].min())
print(new_housedf['Price'].max())

new_housedf


print(apartdf['Price'].min())
print(apartdf['Price'].max())

new_apartdf = remove_outliers(apartdf, ['Price'], 3)

print(new_apartdf['Price'].min())
print(new_apartdf['Price'].max())

new_apartdf