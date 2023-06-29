from sympy import *
x, a, b = symbols('x a b')

print(integrate(((x - a)*(b - a))**0.5, x))

