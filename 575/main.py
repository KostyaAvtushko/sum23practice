from sympy import *
x, a, b = symbols('x a b')

print(limit((1 - sin(x)**(a + b))/(((1 - sin(x)**a)*(1 - sin(x)**b))**0.5), x, pi/2))