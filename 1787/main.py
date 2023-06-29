from sympy import *
x, a = symbols('x a')

print(integrate((x**2)/(a**2 + x**2)**0.5, x))