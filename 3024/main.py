from sympy import *
n, x = symbols('n x')

print(Sum(((-1)**n)*cos(n*x)/(n**2 - 1), (n, 2, oo)).doit().simplify())
