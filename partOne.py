#------------------------
#Leonard Muldoon
#11/16/2023
#--------------

#derivative takes a function, an x value, and an h (represents the difference between x values)
def derivative(f, x, h):
    return (f(x + h) - f(x)) / h

#func is the function for part 1a
def func(x):
    return ((4*x**3) + (2*x**2) - (3*x) + 5)

#calc derivative at x=1
x1 = 1
deltaX = .001
derivativeOfX1 = derivative(func, x1, deltaX)

print("Derivative for part 1a at x= ", x1, " with a delta X of: ", deltaX, " is: ", derivativeOfX1)

"""
Part 1a report

I am choosing a tolerance of 0.0000001 in order to accept a accuracy range of 99.99999% which I deemed close enough to 100% accurate
in most cases. I am starting at h = .001 and will move the 1 one decimal place to the right each time to edit delta x.
"""