import numpy as np

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