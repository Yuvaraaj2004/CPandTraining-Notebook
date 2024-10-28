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
    n, s = M()
    l = GL()
    g = 0
    ans = 0
    for i in range(n):
        if l[i] >= s:
            g += l[i]
        elif l[i] == 0:
            if g:
                ans += 1
                g -= 1
    print(ans)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
