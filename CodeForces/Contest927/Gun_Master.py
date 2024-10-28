'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def M(type): return (map(type, input().split()))


def GL(type): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    a, b = M(int)
    l = GL(int)
    ini = 0 if l[0] <= b else 1
    i, ans = 0, (1 if ini else 0)
    while i < len(l):
        v = i
        while i < len(l) and ((ini and l[i] > b) or (not ini and l[i] <= b)):
            i += 1
        # print(l[v:i])
        ans += 1
        ini = not ini
    print(ans-1)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
