# challenge-data-analysis
Immoweb - Challenge Data Analysis

Melike notes: 
- we can keep zip to create a map afterwards with tableau..
- some garden or terrace column says yes but NaN in the garden or terrace area. So if we set all empty areas to zero, it gives wrong info. (column = column.replace('', np.nan).fillna(0).astype(int)) --> maybe we can fill the area of the ones with yes as mean() of others with surface area?
- however, we can do this on swimming pool or open fire: if it's not yes or an integer, we can just set to zero.
- same on furnished: if yes -> 1, if no or NaN -> 0 
- we can create a scale for Fully equipped kitchen as for Hyper equipped/USA hyper equipped=3, Semi equipped/USA semi equipped=1, Installed/USA installed=1, Not installed/NaN=0 etc..
- same with building condition: new = 3 etc. But I saw that it's removed, but it may be usefull to make predictions on the property prices..
- should we add the info like energy consumption to use afterwards?



Answer the following questions with a vizualization if appropriate:

    How many rows and columns? ok
    What is the correlation between the variables and the price? (Why might that be?)
    How are variables correlated to each other? (Why?)
    Which variables have the greatest influence on the price?
    Which variables have the least influence on the price?
    How many qualitative and quantitative variables are there? How would you transform these values into numerical values?
    Percentage of missing values per column?
