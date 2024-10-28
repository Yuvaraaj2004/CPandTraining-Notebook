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
    a, b, c, d = M()
    if len(set([a, b, c])) <= 2:
        print('YES')
    else:
        print('YES' if abs(a-b) <= d or abs(b-c)
              <= d or abs(c-a) <= d else 'NO')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
