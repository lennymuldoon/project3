#------------------------
#Leonard Muldoon
#11/16/2023
#--------------

#derivative takes a function, an x value, and an h (represents the difference between x values)
def derivative(f, x, h):
    return (f(x + h) - f(x)) / h

#func is the function for part 1 a
def func(x):
    return ((4*x**3) + (2*x**2) - (3*x) + 5)