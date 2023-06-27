from sympy import *
from sympy.abc import n, x

print(Sum(((-1)**(n - 1))*cos(n*x)/(n*(n - 1)), (n, 1, oo)).doit().simplify())
