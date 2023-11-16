#------------------------
#Leonard Muldoon
#11/16/2023
#--------------
#func is the function used for part 2
def func(x):
    return ((.34*x**2) + (2.98*x) + 153)

#finds the integral of functon f starting from point a, to point b, and n is num of rectangles
def integral(f, a, b, n):
    deltaX = (b-a)/n
    area = 0
    for i in range(n):
        height = f(a + i * deltaX)
        area+= height * deltaX
    return area

print(integral(func, 0, 1, 20))
