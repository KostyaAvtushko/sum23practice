from sympy import *

x, a, b, c, d, n = symbols('x a b c d n')
expr = (a*x + b)/(c*x + d)

print(expr.diff((x, n)))
