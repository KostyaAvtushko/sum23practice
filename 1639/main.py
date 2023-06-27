from sympy import *
x = symbols('x')

print(integrate((x**2)/(1 + x**2), x))
