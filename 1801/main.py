from sympy import *
x = symbols('x')

print(integrate((x**3)*(exp(3*x) + exp(-3*x))/2 , x))
