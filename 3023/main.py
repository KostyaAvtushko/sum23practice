from sympy import *
n, x = symbols('n x')

print(Sum(cos(2*n - 1)*x/(2*n - 1)**2, (n, 1, oo)).doit().simplify())