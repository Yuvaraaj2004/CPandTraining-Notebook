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
    a, b = M()
    l = [[2]*b for i in range(a)]
    pos = 0
    for i in range(max(a, b)):
        l[i % a][pos % b] = 3
        pos += 1

    for i in l:
        print(*i)


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
