#Simpson's Rule
x = []
y = []

#Reading file and getting x and f(x) = y
count = 0
with open("Simpson_Rule_input.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
        count += 1
        myList = line.strip().split()
        x += [float(myList[0])]
        y += [float(myList[1])]

#Calculating h
h = x[1] - x[0]

#Display h and number of points
print("h : " + str(h))
print("Number of points : " + str(int(len(y))) + "\n")

#Doing Simpson's Rule method
summ = 0
for i in range(1, len(y)-1):
    if i%2 != 0:
        summ += 4*(y[i])
    else:
        summ += 2*(y[i])

#Display result
res = (h/3)*((y[0]+y[-1]) + summ)
print("Integration result by Simpson's method is: " + str(res))