from sympy import *
x = symbols('x')

print(limit(((1 + 2*x)**0.5 - 3)/(x**0.5 - 2),x, 4))
