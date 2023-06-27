from sympy import *
x = symbols('x')

print(integrate(x*atan(x), x))
