'''
Created By: _Cypher_0101
'''


from math import lcm, log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def M(type=int): return (map(type, input().split()))


def GL(type=int): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def f(s):
    d, t, j = [], 'front', 0
    for ind, i in enumerate(s):
        if j < len(t) and (i == t[j] or i == '?'):
            j = (j+1) % len(t)
            d.append(ind)
    print(d, s)
    return ''.join([i for ind, i in enumerate(s) if ind not in d]) if len(d) == len(t) else s


def b(s, t):
    d, j, f = [],  0, 0
    for ind, i in enumerate(s):
        if j < len(t) and (i == t[j] or (f and (f := (f-1)))):
            j = (j+1) % len(t)
            d.append(ind)
            if j == 0:
                f += 1
    rem = len(d) % len(t)
    d = set(d[rem:])
    print(d, s, len(d), len(s))
    return ''.join([i for ind, i in enumerate(s) if ind not in d]) if len(d) == len(t) else s


def Solve():
    n = int(input())
    s = I()
    while len(s) != len(s := b(s[::-1], 'kacb')[::-1]) and (s := s+'?'):
        print(s)
    while len(s) != len(s := b(s, 'front')) and (s := '?'+s):
        print(s)

    print(len(s))


def primeFactors(n):
    l, i = Counter(), 2
    while i*i <= n:
        while n != 1 and n % i == 0:
            l[i] += 1
            n //= i
        i += 1
    if n != 1:
        l[n] += 1
    return l


if __name__ == "__main__":
    # print(primeFactors(600851475143))
    l = 1
    for i in range(2, 21):
        l = lcm(l, i)
        print(l)
    print(primeFactors(l))
    # Counter({71: 1, 839: 1, 1471: 1, 6857: 1})
    # ans = 6857
    ans = 1
    for k, v in primeFactors(600851475143).items():
        ans *= k**v
    # print(ans)
    # for i in range(int(input())):
    # Solve()
