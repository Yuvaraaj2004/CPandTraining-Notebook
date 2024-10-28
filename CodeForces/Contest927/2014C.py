'''
Created By: _Cypher_0101
'''


from bisect import bisect_left, bisect_right
import decimal
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
    n, lis = II(), sorted(GL())

    def check(mid):
        nav = decimal.Decimal(av+mid)/(n*2)

        return bisect_left(lis, nav)
    if n <= 2:
        print(-1)
    else:
        l, r, av = 0, 10**10, sum(lis)
        while l < r:
            mid = (l+r)//2
            # print(l, r, mid, check(mid))
            if check(mid) > (n)/2:
                r = mid
            else:
                l = mid+1
        print(l)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
