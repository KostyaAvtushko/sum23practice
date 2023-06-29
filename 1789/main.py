from sympy import *
x, a, b = symbols('x a b')

print(integrate(1/((x + a)*(x + b)**0.5), x).doit())