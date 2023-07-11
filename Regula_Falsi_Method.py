#Function
def f(x):
    return (x**3) - (2**((x)**(1/2)))

#Regula Falsi Method
def falsePosition(x0, x1, e):
    step = 1
    print("\n\t------- Regula Falsi Method -------")
    condition = True
    while condition:
        x2 = (x0) - (x1-x0) * (f(x0)/(f(x1)-f(x0)))
        print("Iteration(%d) -> x2 = %0.4f and f(x2) = %0.4f" % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step += 1
        condition = abs(f(x2)) > e
        
        if abs(f(x2)) <= 0.001:
            break

    print("\nRequired root is: %0.4f" % x2)


# Input Section
x0 = 1.0
x1 = 2.0
e = 0.00001

print("First Guess: 1")
print("Second Guess: 2")

#Doing Regula Falsi Method
falsePosition(x0, x1, e)