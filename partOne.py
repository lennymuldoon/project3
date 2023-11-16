#------------------------
#Leonard Muldoon
#11/16/2023
#--------------

import math #this will be used for part 1b

#derivative takes a function, an x value, and an h (represents the difference between x values)
def derivative(f, x, h):
    return (f(x + h) - f(x)) / h

#func is the function for part 1a
def func(x):
    return ((4*x**3) + (2*x**2) - (3*x) + 5)

#calc derivative at x=1 and -3 (swapped values when testing as needed)
x1 = -3
deltaX = 0.000001
derivativeOfX1 = derivative(func, x1, deltaX)

print("Derivative for part 1a at x= ", x1, " with a delta X of: ", deltaX, " is: ", derivativeOfX1)

"""
Part 1a

I am choosing a tolerance of 0.00001 in order to accept a accuracy range of 99.999% which I deemed close enough to 100% accurate
in most cases. I am starting at h (delta X) = .001 and will move the 1 one decimal place to the right each time to edit delta x until I reach the
answer within tolerance (answer within tolerance is when error is < tolerance). Error is calculated by (given value - actual value) / actual value

The actual value of the derivative of x = 1 is 13 and for x = -3 is 93

Run 1:
Derivative for part 1a at x=  1  with a delta X of:  0.001  is:  13.014003999998636
error is 0.001 which is not in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  0.001  is:  92.96600399999022
error is .00036 which is not in my tolerance

Run 2:
Derivative for part 1a at x=  1  with a delta X of:  0.0001  is:  13.001400039982514
error is .0001 which is not in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  0.0001  is:  92.99660004032262
error is .000037 which is not in my tolerance

Run 3:
Derivative for part 1a at x=  1  with a delta X of:  1e-05 (.00001)  is:  13.00014000040761
error is .000011 which is not in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  1e-05 (.00001) is:  92.99966000071434
error is .0000037 which is in my tolerance

Run 4:
Derivative for part 1a at x=  1  with a delta X of:  1e-06 (.000001) is:  13.000014000397186
error is .0000011 which is in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  1e-06 (.000001) is:  92.99996602862848
error is .00000036 which is in my tolerance

I stopped here on run 4 because I have an error which is in my tolerance for both x values. A delta X of .000001 is acceptable for x = 1 and x = 3
"""

#func2 is the function for part 1b
def func2(x):
    return ((x**2) * (math.cos(x)))

#calc derivative at x=0 and pi (swapped values when testing as needed)
x2 = 0
derivativeOfX2 = derivative(func2, x2, deltaX)

print("Derivative for part 1b at x= ", x2, " with a delta X of: ", deltaX, " is: ", derivativeOfX2)

"""
Part 1b

I am going to use the same tolerance as 1a (0.00001) for consisntancy and will start with the delta X that worked for part 1a (.000001) to see if it works here.

The actual value of the derivative of x = 0 is 0 and for x = pi is -6.28319 (pi in the math library is 3.141592653589793)

Run 1:
Derivative for part 1b at x=  0  with a delta X of:  1e-06 (.000001) is:  9.999999999995e-07
error is .000001 which is in my tolerance

Derivative for part 1b at x=  3.141592653589793  with a delta X of:  1e-06 (.000001) is:  -6.283181372523927
error is .0000014 which is in my tolerance

I stopped here on run 1 because I have an error which is in my tolerance for both x values. A delta X of .000001 is acceptable for x = 0 and x = pi
"""