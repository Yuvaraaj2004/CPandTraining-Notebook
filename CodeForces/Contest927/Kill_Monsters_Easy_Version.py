'''
Created By: _Cypher_0101
'''


import bisect
from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush
from bisect import bisect_left

mod = 10**9+7


def M(type=int): return (map(type, input().split()))


def GL(rtype=list, type=int): return rtype(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    n, h, mul = M()
    a, b = [], []
    for x, y in sorted(GL(Counter).items()):
        a.append(x)
        b.append((y > 1)+(b[-1] if b else 0))
    print(a, b)
    c = 0
    ans = 0
    for i in range(bisect_left(a, x)-1, -1, -1):
        ans = max(ans, bisect_left(a, a[i]*mul)+(1 if b[i] > 0 else 0))
        print(ans, i, a[i], b[i])
        c += 1 if b[i] > 1 else 0
    print(ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
