from sympy import *
x = symbols('x')

print(integrate(((1 - 2*x + x**2)**(1/5))/(1 - x)).doit)
