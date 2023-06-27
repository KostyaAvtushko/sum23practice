from sympy import *
x = symbols('x')

print(limit((x**0.5 + x**(1/3) + x**(1/4))/((2*x + 1)**0.5), x, oo))