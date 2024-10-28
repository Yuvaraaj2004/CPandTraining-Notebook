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
    n, k = M()
    l = GL()
    if n == k+1:
        print(sum(l))
    else:
        mx = []
        for i in range(k):
            if mx and mx[0] > l[-1]:
                curm = heappop(mx)
            else:
                curm = l.pop()
            heappush(mx, (l.pop(0)+curm))
            # print(l, mx)
        print(*sorted(mx+l))

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
