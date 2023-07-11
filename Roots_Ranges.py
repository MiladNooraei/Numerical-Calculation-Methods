import math

#input
def f(x):
    return math.sin(31 * x) - 2 * math.cos(23 * x)


def location(min, max, step):

    bounds = []

    # if f(x) multiplied by f(x) is not positive then add x to the bounds list
    index = min
    while index < max:

        if f(index)*f(index+step) <= 0:
            if index + step <= max:
                bounds += [index]

        index += step
    print(" \n Our location step is " + str(step))
    print(" \n!!! This equation has " + str(len(bounds)) +
          " roots in range " + "( " + str(min) + " , " + str(max) + " ) " "!!! \n ")
    print(" >>>>> In these ranges we have a root :")
    for i in bounds:
        print(" >> ( " + str(i) + " , " + str(i+step) + " )")
    print("\n #################################### \n ")

    return bounds


def bisection(first, last):

    min = first
    max = last

    for index in range(1, 11):

        average = (min + max) / 2
        print(" >> Step " + str(index) + " : " + str(average))

        if f(min)*f(average) <= 0:
            max = average
        else:
            min = average
        average = (min + max) / 2

step = 1
list = location(-7, 6.5, step)

for index in list:
    print(" ------------- in " + "( " + str(index) +
          " , " + str(index+step) + " )" + "-------------")
    bisection(index, index + step)
    print("\n")
