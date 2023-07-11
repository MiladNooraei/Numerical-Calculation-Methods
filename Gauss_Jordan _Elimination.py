import numpy as np

#This function gets Coefficients of variables in equations
def getNum(symbols, equationList):
    theList = []
    counter = 0
    while counter != 5:
        for i in range(len(equationList)):
            if symbols[counter] not in equationList:
                theList += [0.0]
                break
            if equationList[i] == symbols[counter]:
                if i == 0:
                    theList += [1.0]
                    break
                elif equationList[i - 1] == "-":
                    theList += [-1.0]
                    break
                elif equationList[i - 1] in symbols:
                    theList += [1.0]
                    break
                elif (i == 1) and (equationList[i - 1] not in symbols):
                    theList += [float(equationList[i - 1])]
                    break
                elif (i > 1) and (equationList[i - 1] not in symbols) and (equationList[i - 2] != "-"):
                    theList += [float(equationList[i - 1])]
                    break
                elif (i > 1) and (equationList[i - 1] not in symbols) and (equationList[i - 2] == "-"):
                    theList += [float(equationList[i - 1]) * (-1)]
                    break
        counter += 1
    return theList


# number of unknowns
n = 5
print('Number of unknowns: ' + str(n))
print("\n")

# Making numpy array of (n x n+1) size and initializing to zero for storing augmented matrix
a = np.zeros((n, n + 1))

# Making numpy array of n size and initializing to zero for storing solution vector
x = np.zeros(n)

inputList = []
equations = ["0.3 X + 9 Y - Z + 3 W - 2 M = 17",
             "7 X + Z - 4 W - M = 3",
             "6 X + 2 Z + 2 Y + M + 8 W = 1",
             "- 1.2 Z + 17 Y + W - X = 15",
             "Y + 2 W + Z - X = -7"]

#Showing equations
print("The equations are :")
for i in equations:
    print(i)
print("\n")

symbols = ["X", "Y", "Z", "W", "M"]
nums = []

for i in equations:
    equation = i
    res = i.split()
    res2 = []
    for i in res:
        if i != "" and i != " " and i != "+" and i != "=":
            res2 += [i]
    inputList += [res2]

for i in inputList:
    theList = getNum(symbols, i)
    theList += [float(i[-1])]
    for i in theList:
        nums += [i]

# Reading augmented matrix coefficients
counter = 0
for i in range(n):
    for j in range(n + 1):
        a[i][j] = nums[counter]
        counter += 1

# Applying Gauss Jordan Elimination
for i in range(n):
    if a[i][i] == 0.0:
        print("Divide by zero detected!")

    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Obtaining Solution
for i in range(n):
    x[i] = a[i][n] / a[i][i]

# Displaying solution
print("Solved values are : ")
for i in range(n):
    print("%s = %0.4f" % (symbols[i], x[i]), end = "\t")