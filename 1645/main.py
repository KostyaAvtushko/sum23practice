from sympy import *
x = symbols('x')

print(integrate((2**(x + 1) - 5**(x - 1))/(10**x), x))