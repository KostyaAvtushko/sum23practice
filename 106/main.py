from sympy import Symbol, oo, limit, S, Max, Min, log, limit_seq, maximum
from sympy.abc import n, k, m
from sympy import sequence

upper_limit = limit_seq(((-1)**n)*n, n)


print((-1)**n)*n)
print("Верхний предел:", upper_limit)
