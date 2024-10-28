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
    n, l = II(), GL(Counter)

    @cache
    def dp(ind=0, a=l[1], b=l[2], c=l[3]):
        if ind == n:
            return 0
        else:
            ans, c = dp(ind+1), Counter()
            for i in range(ind, n):
                c[i]
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
