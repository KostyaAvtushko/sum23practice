
from sympy import *
from numpy import *
x = symbols('x')

print(limit((((exp(pi/x) + exp(-(pi/x)))/2)/(cos(pi/x)))**(x**2), x, oo))
