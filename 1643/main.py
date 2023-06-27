from sympy import *
x = symbols('x')


print(integrate(((x**2 + 1)**0.5 - (x**2 - 1)**0.5) / (x**4 - 1)**0.5, x).doit())
