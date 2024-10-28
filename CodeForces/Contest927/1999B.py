'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def M(type=int): return (map(type, input().split()))


def GL(type=int): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    l = GL()
    a, b = [l[0], l[1]], [l[2], l[3]]
    ans = 0

    def f(x, y):
        # print(x, y)
        return 0 if x[0] == y[0] else (1 if x[0] > y[0] else -1)+(0 if x[1] == y[1] else (1 if x[1] > y[1] else -1))

    val = [0, 0]
    for x in (a, a[::-1]):
        for y in (b, b[::-1]):
            if (v := f(x, y)) > 0:
                val[0] += 1
            elif v < 0:
                val[1] += 1

    print(val[0])
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
