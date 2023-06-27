from sympy import *
x = symbols('x')

print(limit((cos(x*(E**x)) - cos(x*(E**(-x))))/(x**3), x, 0))
