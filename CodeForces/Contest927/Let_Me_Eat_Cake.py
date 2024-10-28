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
    l = GL()
    ans = 0
    while l[0] != l[1]:
        if l[0] > l[1]:
            ans += ceil(l[0]/2)
            l[0] -= ceil(l[0]/2)
        else:
            ans += ceil(l[1]/2)
            l[1] -= ceil(l[1]/2)
        # print(l)
        # break
    print(ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
