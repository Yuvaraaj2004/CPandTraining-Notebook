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
    n = II()
    adj = [set() for i in range(n)]
    for i in range(n-1):
        a, b = M()
        adj[a-1].add(b-1)
        adj[b-1].add(a-1)
    # adj.sort(key=lambda x: len(x))
    # print(adj)
    q = [3 if len(i) == 1 else 2 for ind, i in enumerate(adj)]
    print(sum(q))
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
