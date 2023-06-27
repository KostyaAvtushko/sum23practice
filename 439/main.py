from sympy import *

x, a = symbols('x a')

print(limit((x**0.5 - a**0.5 + (x - a)**0.5)/((x**2 - a**2)**0.5), x, a))
