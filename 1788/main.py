from sympy import *
x, a = symbols('x a')

print(integrate(((x - a)/(x + a))**0.5, x).doit())
