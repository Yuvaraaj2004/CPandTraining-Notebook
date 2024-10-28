'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict, deque
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def M(type=int): return (map(type, input().split()))


def GL(type=int): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    l = sorted([(i, ind) for ind, i in enumerate(GL())])
    # print(sorted([(int(y), x)
    #   for x, y in zip(l, "3 3 4 3 1 3 3 0 2 3 2 2 1 3 2 3".split())]))
    ini, ans = 0, [0]*16
    for i, (x, y) in enumerate(l):
        if (i+1) & (i) == 0:
            ini += 1
        ans[y] = ini-1
    print(*ans)


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
