from sympy import *
x = symbols('x')


print(integrate((x)/((1 - x**2)**0.5), x))