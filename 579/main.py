from sympy import *
x = symbols('x')

print(limit(x - log((exp(x) + exp(-x))/2) , x, oo))