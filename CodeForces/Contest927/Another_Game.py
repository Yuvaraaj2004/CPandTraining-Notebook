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


def check(mid):
    pass


def Solve():
    n, lis = II(), GL()
    # l, r = 0, n*2
    # while l < r:
    #     mid = (l+r)//2
    #     if check(mid):
    #         r = mid
    #     else:
    #         l = mid+1
    d, ans = {}, 0
    for ind in range(n-1, -1, -1):
        i = lis[ind]
        if i != lis[i-1]:
            if i in d:
                ans = max(d[i]+i, ans)
                d[ind+1] = d[i]
                del d[i]
            else:
                d[ind+1] = i
        print(d)

    print(ans)


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
