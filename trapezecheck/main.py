from sympy import *
x = symbols('x')

print(integrate((x**x)*(1 + log(x)), (x, 1, 3)))