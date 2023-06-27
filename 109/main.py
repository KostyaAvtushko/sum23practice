from sympy import Symbol, oo, limit, S, Max, Min, log, limit_seq, maximum, cos, pi, sin
from sympy.abc import n

print(limit_seq(1 + n*sin((pi*n)/2)))
