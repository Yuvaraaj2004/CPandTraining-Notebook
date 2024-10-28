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
    l, r = a, b+a-1
    # print(l != r, (r - l + 1) //
    #       2, (l == r and l & 1 == 0))
    print('YES' if l != r and (((r - l + 1) // 2)
          & 1 == 0) or (l == r and l & 1 == 0) else 'NO')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
