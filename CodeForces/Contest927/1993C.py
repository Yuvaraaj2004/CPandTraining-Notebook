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


def GL(type=int): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    a, b = M()
    l = sorted(GL())
    mod = sorted(set([i % (2*b) for i in l]))
    if mod[-1]-mod[0] < b:
        v, mx = [], max(l)
        for i in l:
            v.append((mx-i)//(2*b)*(2*b)+(mx-i) % (b))
        print(v, end=' ')
    else:
        print(-1, end=' ')
    print(mod)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
