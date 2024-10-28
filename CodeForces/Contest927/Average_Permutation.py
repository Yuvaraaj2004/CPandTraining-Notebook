'''
Created at: 13-July-24 09:37
Created By: _Cypher_0101
'''

from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from typing import *


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


def primeFactors(n):
    l = Counter()
    for i in range(2, int(sqrt(n)) + 1):
        while n != 1 and n % i == 0:
            l[i] += 1
            n //= i
        if n == 1:
            return l
    if n != 1:
        l[n] += 1
    return l


def exists(x, y, nums):
    return lambda (x, y): x >= 0 and y >= 0 and x < len(nums) and y < len(nums[i])


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


def GetL(): return map(int, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def Solve():

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
