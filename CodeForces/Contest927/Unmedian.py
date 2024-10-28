'''
Created at: 23-October-24 20:33
'''

from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from typing import *
from heapq import heapify, heappop, heappush


mod = 10**9+7
def gcd(x, y): return (y) if x == 0 else gcd(y % x, x)


def Seieve(n):
    prime, i = [True] * (n + 1), 2
    l = []
    while i * i <= n:
        if prime[i]:
            l.append(i)
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1
    return [ind for ind, i in enumerate(prime) if i][2:]


def getBits(n):
    c, l = 0, []
    while n:
        if n & 1:
            l.append(c)
        n >>= 1
        c += 1
    return l


def exists(nums):
    return lambda x, y: x >= 0 and y >= 0 and x < len(nums) and y < len(nums[i])


def BE(b, e, mod=mod):
    b %= mod
    res = 1
    while e:
        if e & 1:
            res = (res * b) % mod
        b = (b * b) % mod
        e >>= 1
    return res


@cache
def fact(n): return 1 if n <= 1 else (n * fact(n - 1) % mod)


def M(type=int): return (map(type, input().split()))


def GL(rtype=list, type=int): return rtype(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def p(*args): print(*args)


def Solve():
    n, l = II(), GL()
    mn, mx = 0, 0
    for ind, i in enumerate(l):
        if l[mn] > i:
            mn = ind
        if l[mx] < i:
            mx = ind
    if mx < mn:
        print(-1)
    elif mn == mx:
        print(2)
    else:
        mx1 = mn
        for i in range(mn+1, mx):
            if l[mx1] < i:
                mx1 = ind
        if l[mx1] > min(l[mx+1:]):
            for i in range(mx, mx1, -1):

            return

    p(mn, mx, l[mx], l[mn])
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
