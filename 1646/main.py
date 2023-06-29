from sympy import *
x = symbols('x')

print(integrate((E**(3*x) + 1)/(E**x + 1), x))
