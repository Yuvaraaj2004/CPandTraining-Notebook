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


def GL(rtype=list, type=int): return rtype(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    a, b, c = M()
    d = 0
    while c-d > 0 and (b)*(100-d*a)/100 > c-d:
        # print((b)*(100-d*a)/100, c-d)
        d += 1
    print(d if (b)*(100-d*a)/100 <= c-d else -1)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
