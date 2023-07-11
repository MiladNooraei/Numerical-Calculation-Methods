#Second derivative using Central Difference Method
import matplotlib.pyplot as plt
x = []
y = []

#Reading file and getting x and f(x) = y
count = 0
with open("deta.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
        count += 1
        myList = line.strip().split()
        x += [float(myList[0])]
        y += [float(myList[1])]

#New x's and their Second derivative values using central difference
newX = []
newY = []

#Calculating h
h = x[1] - x[0]

#Doing Second derivative Central Difference Method and displaying result
for i in range(5, 9992):
    newX += [x[i]]
    newY += [(y[i+1]-(2*y[i])+y[i-1])/(h**2)]
    print("((%f) - (%f) + (%f))/(%f) -> %f" % (y[i+1], 2*y[i], y[i-1], h**2, (y[i+1]-(2*y[i])+y[i-1])/(h**2)))
    
#Plotting the graph
plt.plot(newX, newY)
plt.xlabel("X")
plt.ylabel("Y\"")
plt.title("Graph")
plt.show()