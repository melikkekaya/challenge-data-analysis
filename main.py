import pandas as pd
import re
import numpy as np

df_main = pd.read_csv("properties_data.csv")

df = df_main[["id","location","Zip","Type","Subtype",
    "Price","Transaction Type","Bedrooms","Living area","Kitchen type",
    "Furnished","How many fireplaces?","Terrace","Terrace surface",
    "Garden","Garden surface","Surface of the plot","Number of frontages",
    "Swimming pool","Building condition","Primary energy consumption","CO₂ emission"]]

df.info()

df = df.set_index("id")

df = df.drop(df[df["Type"]=="house group"].index)
df = df.drop(df[df["Type"]=="apartment group"].index)

def clean_and_convert(column):
    column = column.apply(lambda x: re.sub('\D+', '', str(x)))
    # column = column.replace('', np.nan).fillna(0).astype(int)
    return column

df['Living area'] = clean_and_convert(df['Living area'])
df['Terrace surface'] = clean_and_convert(df['Terrace surface'])
df['Garden surface'] = clean_and_convert(df['Garden surface'])
df['Surface of the plot'] = clean_and_convert(df['Surface of the plot'])
df['Primary energy consumption'] = clean_and_convert(df['Primary energy consumption'])
df['CO₂ emission'] = clean_and_convert(df['CO₂ emission'])

df
df.info()

# to change garden column into 1 and 0s
df["Garden"] = np.where((df["Garden"] == "Yes") & (df["Garden surface"] == ""), 1, df["Garden"])
df["Garden"] = np.where((df["Garden"] != "Yes") & (df["Garden surface"] != ""), 1, df["Garden"])
df["Garden"] = df["Garden"].replace("",np.nan).fillna(0).astype(int)

# to change terrace column into 1 and 0s
df["Terrace"] = np.where((df["Terrace"] == "Yes") & (df["Terrace surface"] == ""), 1, df["Terrace"])
df["Terrace"] = np.where((df["Terrace"] != "Yes") & (df["Terrace surface"] != ""), 1, df["Terrace"])
df["Terrace"] = df["Terrace"].replace("",np.nan).fillna(0).astype(int)

def nan_replacement(column):
    column = column.replace("Yes",1)
    column = column.replace("No",0)
    column = column.replace('', np.nan).fillna(0)
    return column

df['Furnished'] = nan_replacement(df['Furnished'])
df['Swimming pool'] = nan_replacement(df['Swimming pool'])
df['How many fireplaces?'] = nan_replacement(df['How many fireplaces?'])

#Missing values fillied with 1
df["Primary energy consumption"] = np.where((df["Primary energy consumption"] != int) & (df["Primary energy consumption"] == ""), 0, df["Primary energy consumption"])
df["Primary energy consumption"] = df["Primary energy consumption"].replace("",np.nan).fillna(0).astype(int)

#New column with energy classes 
conditions = [
    (df['Primary energy consumption']>1)&(df['Primary energy consumption']<100),
    (df['Primary energy consumption']>100)&(df['Primary energy consumption']<200),
    (df['Primary energy consumption']>200)&(df['Primary energy consumption']<300),
    (df['Primary energy consumption']>300)&(df['Primary energy consumption']<400),
    (df['Primary energy consumption']>400)&(df['Primary energy consumption']<500),
    (df['Primary energy consumption']>500)&(df['Primary energy consumption']<600),
    (df['Primary energy consumption']>600)
]

values = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


df['Energy_classes'] = np.select(conditions, values)


#df.to_csv('almost_clean.csv')

