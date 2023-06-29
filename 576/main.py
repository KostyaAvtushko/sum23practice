from sympy import *
x = symbols('x')

print("576. a) " + str((limit(((exp(x) - exp(-x))/2)/(x), x, 0))))
print("576. b) " + str((limit(((exp(x) + exp(-x))/2 - 1)/(x**2), x, 0))))
print("576. c) " + str((limit(((exp(x) - exp(-x))/(exp(x) + exp(-x)))/x, x, 0))))