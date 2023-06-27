from sympy import Symbol, oo, limit, S, Max, Min, log, limit_seq, maximum, cos, pi
from sympy.abc import n, k, m
from sympy import sequence
import numpy

print("101. a) " + str(limit_seq(1 - 1/n, n)))

print("101. б) " + str(limit_seq(((-1)**(n-1))*(2 + 3/n), n)))

print("102. " + str(limit_seq(((-1)**n / n) + ((1 + (-1)**n) / 2), n)))

print("103. " + str(limit_seq(1 + n * cos(n*pi) / (n + 1) ,n)))
