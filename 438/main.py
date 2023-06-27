from sympy import *
x = symbols('x')

print(limit(((1 - x)**0.5 - 3)/(2 + x**(1/3)), x, -8))