from sympy import *
x, a = symbols('x a')

print("578. a) " + str(limit((((exp(x) - exp(-x))/2) - ((exp(a) - exp(-a))/2))/(x - a), x, a)))
