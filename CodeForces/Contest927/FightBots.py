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


d = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}


def Solve():
    a, b, c = M()
    x, y = 0, 0
    f = 0

    for ind, i in enumerate(I()):
        v2, v1 = d[i]
        x, y = x+v1, y+v2
        if not f and abs(x-b) + abs(y-c) == ind+1:
            f = 1
            print('Yes')
            break
    # print('Yes' if abs(x-b) + abs(y-c) <= a else 'No')
    if f == 0:
        print('No')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
