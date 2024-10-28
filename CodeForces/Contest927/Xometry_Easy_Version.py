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
    n, lis = II(), GL()
    d = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            d[lis[i] ^ lis[j]].append((i, j))

    print(d)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
