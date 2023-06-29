from sympy import *
x = symbols('x')

print("577. a) " + str((limit(((exp(x) - exp(-x))/2)**2/(log((exp(3*x) + exp(-3*x))/2)), x, 0))))
print("577. б) " + str((limit( ((exp(sqrt(x**2 + x)) - exp(sqrt(x**2 + x)))/2 - (exp(sqrt(x**2 - x)) - exp(sqrt(x**2 - x)))/2)/((exp(x) + exp(-x))/2), x, oo))))