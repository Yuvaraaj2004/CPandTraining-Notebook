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
    n, s, m = M()
    last, f = 0, False
    for i in range(n):
        a, b = M()
        if a-last >= s:
            f = True
        last = b
    if m-last >= s:
        f = True
    print('YES' if f else 'NO')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
