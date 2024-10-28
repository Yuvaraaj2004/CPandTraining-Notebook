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
    n, arr = II(), GL()
    l, r = 0, n-1
    while l < n and arr[l] < 0:
        l += 1
    while r > l and arr[r] < 0:
        r -= 1
    ans = 0
    for i in range(l, r+1):
        if arr[i] < 0:
            ans += 1
    print(ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
