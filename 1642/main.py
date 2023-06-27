from sympy import *
x = symbols('x')


print(integrate(((1 + x**2)**0.5 + (1 - x**2)**0.5)/(1 - x**4)**0.5, x))
