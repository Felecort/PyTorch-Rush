from functools import reduce
from operator import mul

def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return set(primfac)


def proper_fractions(n):
    if n == 1: return 0
    return int(n * reduce(mul, [1 - 1/x for x in primfacs(n)]))

if __name__ == "__main__":
    print(proper_fractions(2))
