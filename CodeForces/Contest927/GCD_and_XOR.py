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


def gcd(x, y): return (y) if x == 0 else gcd(y % x, x)


def Solve():
    n, k = M()
    l = GL(rtype=set)

    if all(x == k for x in l):
        print(0)
    elif all(gcd(x, k) == k for x in l) or len(set(l)) == 1:
        print(1)
    else:
        print(2)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
