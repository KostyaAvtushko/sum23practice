from sympy import *
x = symbols('x')

print(integrate((1 - sin(2*x))**0.5, x))