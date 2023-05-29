"""Filling missing values in 
based on Multivariate Approach:
pip install scipy,  Scikit-learn, sklearn, run it after outliers are removed"""
#I use my df for houses and apartments: df_houses, df_apartments. And columns which are "params_for_corr", see below:
#params_for_corr = ['Price','Living area','Building Cond. values', 'Number of facades', 'Kitchen values', 'Surface of the land', 'Primary energy consumption', 'Energy efficiency', 'Terrace','Terrace surface','Garden', 'Garden surface']
#They are the same for houses and apartments.  Feel free to modify if needed. The column 'Energy_class' was renamed to 'Energy efficiency'.
columns = params_for_corr 

impute_it = IterativeImputer()
np_array_houses = impute_it.fit_transform(df_houses).astype(int)
np_array_apartments = impute_it.fit_transform(df_apartments).astype(int)


complete_df_houses = pd.DataFrame(np_array_houses,columns = columns)
complete_df_apartments = pd.DataFrame(np_array_houses, columns = columns)

complete_df_houses.head(10)
complete_df_apartments.head(10)

#new_df_houses.to_csv('missing_values_filled_houses.csv')

#complete_df_apartments.to_csv('apartments_filled.csv')
