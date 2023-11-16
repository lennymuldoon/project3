#------------------------
#Leonard Muldoon
#11/16/2023
#--------------

#func is the function used for part 2
def func(x):
    return ((.34*x**2) + (2.98*x) + 1.53)

#finds the integral of functon f starting from point a, to point b, and n is num of rectangles
def integral(f, a, b, n):
    deltaX = (b-a)/n
    area = 0
    for i in range(n):
        height = f(a + i * deltaX)
        area+= height * deltaX
    return area

#finds the integral within tolerance with num rectangles and returns the num rectangles and area.
def integralWithTol(a, b, n, t):
    n2 = n * 2
    area = integral(func, a, b, n)
    areaPrime = integral(func, a, b, n2)
    while abs(area - areaPrime) >= t:
        n2 *= 2
        area = areaPrime
        areaPrime = integral(func, a, b, n2)
    return n2, areaPrime

a = 2
b = 4
numRect = 10
tol = 0.00001
n, areaFinal = integralWithTol(a, b, numRect, tol)
print("Area: ", areaFinal, " Number of rectangles: ", n)