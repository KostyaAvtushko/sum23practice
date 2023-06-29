from sympy import *
from numpy import *
x, n = symbols('x n')
expr = x*(E**x - E**(-x))/2

print(expr.diff((x, n)))
