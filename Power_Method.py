import numpy as np

#input matrix:
#[9, -3, -6]
#[2, 8, 2]
#[-5, 10, 7]


#inverse matrix:
#[1.0000000000000007, -1.0833333333333344, 1.1666666666666676]
#[-0.6666666666666672, 0.9166666666666674, -0.8333333333333339]
#[1.666666666666668, -2.0833333333333353, 2.1666666666666683]

#Making numpy array of 3x3 size and initializing to zero for storing matrix
n = 3
a = np.zeros((n,n))

#Storing max lambda and min lambda
lmaxmin = []

#Creating our matrix
matrix = [[9, -3, -6], [2, 8, 2], [-5, 10, 7]]
inversedmatrix = np.linalg.inv(matrix)

mat = []
for i in range(3):
    for j in range(3):
        mat += [matrix[i][j]]
invmat = []
for i in range(3):
    for j in range(3):
        invmat += [inversedmatrix[i][j]]

counter = 0
for i in range(n):
    for j in range(n):
        a[i][j] = float(mat[counter])
        counter += 1

#Creating x0 = [1, 1, 1]
x = np.zeros((n))
for i in range(n):
    x[i] = 1.0

#maximum number of steps
maxStep = 100

# Power Method Implementation
lambda_old = 1.0
condition =  True
step = 1
while condition:
    x = np.matmul(a,x)
    lambda_new = max(abs(x))
    x = x/lambda_new
    print("\nSTEP %d ->" %(step))
    print("lambda max = %0.4f" %(lambda_new))
    print("X%d: "%(step))
    for i in range(n):
        print("%0.3f\t" % (x[i]))
    step = step + 1
    if step > maxStep:
        lmaxmin += [lambda_new]
        break
   
#Creating our inverse matrix
counter = 0
for i in range(n):
    for j in range(n):
        a[i][j] = float(invmat[counter])
        counter += 1

#Creating x0 = [1, 1, 1]
x = np.zeros((n))
for i in range(n):
    x[i] = 1.0
    
#maximum number of steps
maxStep = 4
    
#Inverse Power Method Implementation
lambda_old = 1.0
condition =  True
step = 1
while condition:
    x = np.matmul(a,x)
    lambda_new = max(abs(x))
    x = x/lambda_new
    lambda_new = 1/lambda_new
    print("\nSTEP %d ->" %(step))
    print("lambda min = %0.4f" %(lambda_new))
    print("X%d: "%(step))
    for i in range(n):
        print("%0.3f\t" % (x[i]))
    step = step + 1
    if step > maxStep:
        lmaxmin += [lambda_new]
        break
    
print("\nMax Lambda : " + str(lmaxmin[0]))
print("Min Lambda : " + str(lmaxmin[1]))