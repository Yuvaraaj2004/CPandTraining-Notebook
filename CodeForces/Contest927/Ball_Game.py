'''
Created By: _Cypher_0101
'''


from decimal import Decimal
from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def M(type=int): return (map(type, input().split()))


def GL(rtype=list, type=int): return rtype(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    n = II()
    pos, speed = GL(), GL()
    l = [[Decimal(x) / Decimal(y), x, y] for x, y in zip(pos, speed)]
    l.sort(key=lambda x: (x[0], x[1]))
    ans = 0
    i = 0
    while i < n:
        j = i+1
        while j < n and l[j][1] < l[i][1]:
            j += 1
        ans += 1
        i = j
    # print(l)
    print(ans)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
