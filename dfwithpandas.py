#importing numpy and pandas
import numpy as np
import pandas as pd

#Loading a first series
Capacity = pd.Series(data=[60432,55097,39460])
print(Capacity)

#Changing labels for Series
Capacity_pl = pd.Series(data=[42837,42771,41620,31103
                            ,24563,22372,21163,18018],
                     index=["Enea Arena","Tarczynski Arena","Polsat Plus Arena",
                            "Stadion Miesjski Warszawa","Arena Zabrze","Stadion Miejski Bialystok",
                            "Stadion Miesjski Szczecin","Stadion Widzewa"])
print(Capacity_pl)

#We can now access the series by index
print(Capacity_pl["Polsat Plus Arena"])

#We can get the same output using a dictionary
CapacityDict = {'Enea Arena':42837,
                'Tarczynski Arena':42771,
                'Arena Zabrze':24563}

Capacity_pl2 = pd.Series(CapacityDict)
print(Capacity_pl2)

#--- Now lets see how to work with data frames ---
#Lets build a scouting report for 4 imaginary players
PlayerList = ["Pagbo","Grazemen","Cantay","Ravane"]
SkillList=["Shooting","Passing","Defending"]

#For this example, we have a random number generator for our scout
#I wouldn't recommend this for an actual team
ScoresArray = np.random.randint(1,10,(4,3))

df = pd.DataFrame(data=ScoresArray, index=PlayerList, columns=SkillList)
print(df)

#Square brackets for columns
#If the result looks familiar, that's because DataFrame columns are series!
print(df['Shooting'])

#For rows, we use .loc if we use a name
#Turns out that DataFrame rows are also series!
print(df.loc['Pagbo'])

#Or if we use a index number, .iloc
print(df.iloc[1:3])

#Lets add a communication on the pitch coloumn

df['Communication'] = np.random.randint(1,10,4)
print(df)

#Now lets drop the defending coloumn as we are looking for a new striker

df = df.drop('Defending', axis=1)
print(df)

#We can also drop a row
#Lets drop Pagbo as he is not interested signing for our club

df = df.drop('Pagbo',axis=0)
print(df)

#We can also decide to select and display only rows or coloumns following certain criteria

#Lets check, where our players meet our criteria
print(df>5)

#Now lets apply this to a certain column
print(df['Shooting']>5)

#Now lets display the data frame only with players matching our criteria by subsetting it
print(df[df['Shooting']>5])

#Lets set up a new data frame for transfer targets
dftrans = pd.DataFrame({'Wage':[150000,123000,np.nan],
'GoalBonus':[4000,np.nan,np.nan],
'ImageRights':[50000,70000,100000]},
index=['Konda','Makho','Grey'],
columns=['Wage','GoalBonus','ImageRights'])

print(dftrans)

#We could drop rows or columns with missing values
dftra_row = dftrans.dropna()
print(dftra_row)

dftra_col = dftrans.dropna(axis=1)
print(dftra_col)

#We can also just drop rows/columns with missing values beyond a threshold
dftra_row = dftrans.dropna(thresh=2)
print(dftra_row)

#Sometimes deleting rows is a bit overreaction so we can fill the missing values
dftra_row = dftrans.fillna(value=0)
print(dftra_row)

#We can also calculate a value and fill issing values with that
#For example the averges
dftra_row = dftrans['Wage'].fillna(value=dftrans['Wage'].mean())
print(dftra_row)