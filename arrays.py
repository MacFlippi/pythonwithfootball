import numpy as np

#--- Setting up arrays with Numpy ---
GKNames = ["Kaller","Fradeel","Hayward","Honeyman"]
GKHeights = [184,188,191,193]
GKWeights = [81,85,103,99]

GKMatrix = [GKNames,GKHeights,GKWeights]

print(np.array(GKMatrix))

#With 'arange', we can create arrays just like we created lists with 'range'
#This gives us an array ranging from the numbers in the arguments

print(np.arange(0,12))

#Want a blank array? Create it full of zeros with 'zeros'
#The argument within it create the shape of a 2d or 3d array
print(np.zeros((3,11)))

#Hate zeros? Why not use 'ones'?!
print(np.ones((3,11)))

#What is the largest height, .max()?
GKHeights = np.array(GKHeights)
print(GKHeights.max())

#What location is the max, .argmax()?
print(GKHeights.argmax())

#Can I use this method to locate the player's name?
#Instead of a number in the square brackets, I can just put this method

print(GKNames[GKHeights.argmax()])

#--- Indexing NumPy Arrays ---
#Setting up an arry for WCs every 4 years since 1930
WCYears = np.arange(1930,2022,4)
#No World Cup in 1942 or 1946
WCYears = np.delete(WCYears,(3,4))
print(WCYears)
#What year was the third World Cup held?
# 2 as in pyhton arrays start with position 0
WCYears[2]

#Create our 2d array
WCYears = [1998,2002,2006,2010,2014,2018]
WCHosts = ["France","Japan/Korea","Germany","South Africa","Brazil","Russia"]
WCWinners = ["France","Brazil","Italy","Spain","Germany","France"]

WCArray = np.array((WCYears,WCHosts,WCWinners))
print(WCArray)

#2010 is the third year, find the host in the second row
print(WCArray[1,2])

#Find the winner and host of the last World Cup
#Negative selection!
print(WCArray[2,-1], WCArray[1,-1])

#NumPy allows to select values based on criteria
WCYears = np.array([1966,1970,1974,1978])
WCTopScorers = np.array(["Eusebio","Muller","Lato","Kempes"])
WCGoals = np.array([9,10,7,6])

#Where does the top scorer score more than 8 goals?
print(WCGoals > 8)

#Not particularly useful, but we can then use bracket selection with this!
print(WCTopScorers[(WCGoals>8)])