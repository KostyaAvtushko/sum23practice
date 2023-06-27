from sympy import *
x = symbols('x')


print(limit((2*E**(x/(x+1)) - 1)**((x**2 + 1)/(x)) ,x, 0))