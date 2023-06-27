from sympy import *
x = symbols('x')

print(limit(((x + 13)**0.5 - 2*(x + 1)**0.5)/(x**2 - 9),x, 3))