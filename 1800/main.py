from sympy import *
x = symbols('x')

print(integrate(x*(exp(x) - exp(-x))/2, x))