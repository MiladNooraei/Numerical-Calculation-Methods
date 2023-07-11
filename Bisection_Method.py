# Defining Function
def f(x):
    return (x**3)+(4*(x**2))-2

#Bisection Method
def bisection(x0, x1, e):
    step = 1
    print("\n\t------- BISECTION METHOD -------")
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print("Iteration(%d) -> x2 = %0.3f and f(x2) = %0.3f" % (step, x2, f(x2)))
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step += 1
        condition = abs(f(x2)) > e
        
        if abs(f(x2)) <= 0.004:
            break

    print("\nRequired Root is : %0.3f" % x2)


x0 = 0.0
x1 = 1.0
e = 0.00001


print("First Guess: 0")
print("Second Guess: 1")

#Doing Bisection Method
bisection(x0, x1, e)