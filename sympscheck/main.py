from sympy import *
from sympy.abc import x

print(integrate(log(x)/(x*sqrt(1 + log(x))), (x, 1, 3.5)))
