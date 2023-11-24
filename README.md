# project3
This is a project from computational thinking using Numerical Analysis
Part 1 -- Numerical Differentiation:

a. Let f(x) = 4x^3 + 2x^2 - 3x + 5.
Approximate the derivative (also known as the slope of the tangent line and the instantaneous rate of change) of f(x) at x = a
Use the following technique:
choose a value for your acceptable error, aka your tolerance.
choose an initial value for h (which represents the difference between x values)
calculate [f(a+ h) – f(a)]/h for decreasing values of h
continue systematically decreasing h until the value of the differences of calculated quantites between steps is lower than your acceptable error.
Do the above algorithm twice -- once for x = 1 and a second time for x = -3 (that is let a = 1 and then let a = -3 in the above calculations to find the derivative of f(x) at two different points).

Report your answers, your initial value of h, the method used to modify h, the value of h when you halted, and the error you used. (answers for derivative of f(x) at x = 1 and x = -3 respectivelly are 13 and 93).

b. Repeat the above for this function -- f(x) = x^2 *cos(x) at x = 0 and x = PI

Part 2 -- Numerical Integration: 

Find the area below the curve of f(x) = .34x^2 + 2.98x + 1.53 from x = 2 to x = 4 and above the x axis. Use the method of rectangles as described in class.
Choose a tolerance, tol,  and an initial number of sub-intervals, n. Calculate the approximate area. Repeat the calculation with a greater n and continue the process until successive approximations have a difference less than tol. Report all choices and results.
