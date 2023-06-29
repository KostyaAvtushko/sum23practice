from sympy import *
x = symbols('x')

print(integrate(1 + cos(x) + sin(x), x))