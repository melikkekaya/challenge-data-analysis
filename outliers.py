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

housedf