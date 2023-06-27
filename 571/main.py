from sympy import *
x = symbols('x')

print(limit(((1 + x*sin(x))**0.5 - 1)/(E**(x**2) - 1),x, 0))

