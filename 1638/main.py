from sympy import *
x = symbols('x')


print(integrate(((x**4 + x**(-4) + 2)**0.5/(x**3)), x).doit())
