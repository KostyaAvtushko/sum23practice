from sympy import *
x = symbols('x')


print(limit((2 - x)**(1/(cos((pi*x)/2))), x, 1))