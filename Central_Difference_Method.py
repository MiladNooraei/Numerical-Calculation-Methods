#Central Difference Method
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

#New x's and their central difference values
newX = []
newY = []

#Doing Central Difference Method and displaying result
for i in range(1, len(x)-1):
    newX += [x[i]]
    newY += [(y[i+1]-y[i-1])/(x[i+1]-x[i-1])]
    print("((%f) - (%f))/((%f) - (%f)) -> %f" % (y[i+1], y[i-1], x[i+1], x[i-1], (y[i+1]-y[i-1])/(x[i+1]-x[i-1])))
    
#Plotting the graph
plt.plot(newX, newY)
plt.xlabel("X")
plt.ylabel("Y'")
plt.title("Graph")
plt.show()