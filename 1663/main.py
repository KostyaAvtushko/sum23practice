from sympy import *
x = symbols('x')

print(integrate(1/((2 - 3*x**2)**0.5), x).doit())
