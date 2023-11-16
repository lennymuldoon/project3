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

#calc derivative at x=1 and -3 (swapped values when testing as needed)
x1 = -3
deltaX = 0.0000001
derivativeOfX1 = derivative(func, x1, deltaX)

print("Derivative for part 1a at x= ", x1, " with a delta X of: ", deltaX, " is: ", derivativeOfX1)

"""
Part 1a

I am choosing a tolerance of 0.00001 in order to accept a accuracy range of 99.999% which I deemed close enough to 100% accurate
in most cases. I am starting at h (delta X) = .001 and will move the 1 one decimal place to the right each time to edit delta x until I reach the
answer within tolerance.

Run 1:
Derivative for part 1a at x=  1  with a delta X of:  0.001  is:  13.014003999998636
error is .01 which is not in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  0.001  is:  92.96600399999022
error is .004 which is not in my tolerance

Run 2:
Derivative for part 1a at x=  1  with a delta X of:  0.0001  is:  13.001400039982514
error is .001 which is not in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  0.0001  is:  92.99660004032262
error is .0034 which is not in my tolerance

Run 3:
Derivative for part 1a at x=  1  with a delta X of:  1e-05 (.00001)  is:  13.00014000040761
error is .0001 which is not in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  1e-05 (.00001) is:  92.99966000071434
error is .00034 which is not in my tolerance

Run 4:
Derivative for part 1a at x=  1  with a delta X of:  1e-06 (.000001) is:  13.000014000397186
error is .00001 which is in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  1e-06 (.000001) is:  92.99996602862848
error is .000034 which is not in my tolerance

Run 5:
Derivative for part 1a at x=  1  with a delta X of:  1e-07 (.0000001) is:  13.000001413132622
error is .000001 which is in my tolerance

Derivative for part 1a at x=  -3  with a delta X of:  1e-07 (.0000001) is:  92.99999661038783
error is .0000034 which is in my tolerance

I stopped here on run 6 because I have an error which is in my tolerance. A delta X of .0000001 is acceptable for x = 1 and x = 3
"""