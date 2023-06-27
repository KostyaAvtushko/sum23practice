from sympy import *
x = symbols('x')


print(integrate((x**2)*((1 + x**3)**(1/3))), x)
