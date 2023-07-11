#Function
def f(x):
    return (x**3) - (x**4 + x**2 + 5)**(1/3)

#Derivative of function
def g(x):
    return (3*x**2) - ((4*x**3 + 2*x)/(3*(x**4 + x**2 + 5)**(2/3)))

#Newton Raphson Method
def newtonRaphson(x0, e, N):
    print("\n\t------- NEWTON RAPHSON METHOD -------")
    step = 1
    flag = 1
    #condition = True
    while step < 17:
        if g(x0) == 0.0:
            print("Divide by zero error!")
            break
        
        x1 = x0 - (f(x0)/g(x0))
        print("Iteration(%d) -> x1 = %0.4f and f(x1) = %0.4f" % (step, x1, f(x1)))
        x0 = x1
        step += 1
        
        if step > N:
            flag = 0
            print("\nRequired root is: %0.4f" % x1)
            break
        
        condition = abs(f(x1)) > e
    
    if flag == 1:
        print("\nRequired root is: %0.4f" % x1)
    else:
        print("\nNot Convergent.")


#Input Section
x0 = 1.5
e = 0.000001
N = 15

print("First Guess: 1.5")
print("Number of steps : 15")

#Doing Newton Raphson Method
newtonRaphson(x0, e, N)