from sympy import *

x = symbols('x')
print(limit((x + (x + x**0.5)**0.5)**0.5/((x + 1)**0.5),x , oo))