#------------------------
#Leonard Muldoon
#11/16/2023
#--------------

#derivative takes a function, an x value, and an h (represents the difference between x values)
def derivative(f, x, h):
    return (f(x + h) - f(x)) / h

