'''
Created at: 31-July-24 14:25
Created By: _Cypher_0101
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


def M(type): return (map(type, input().split()))


def GL(type): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def p(*args): print(*args)


def Solve():
    a, b = M(int)
    s, t = I(), I()
    if s.count('1') != t.count('1'):
        print('NO')
    else:
        a, b = 0, 0
        ans = 0
        for ind, (x, y) in enumerate(zip(s, t)):
            if x == y:
                continue
            else:
                if x == '1':
                    if a:
                        a -= 1
                        ans += 1
                    else:
                        b += 1
                elif x == '0':
                    if b:
                        b -= 1
                        ans += 1
                    else:
                        a += 1
        print('YES' if ans <= b else 'NO')

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
