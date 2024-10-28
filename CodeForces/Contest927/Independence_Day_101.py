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
    l = list(-i for i in GL())
    heapify(l)
    while len(l) > 1:
        (a), (c) = heappop(l), heappop(l)
        if a == 0 or c == 0:
            heappush(l, min(0, c+1))
            heappush(l, min(0, a+1))
            break
        heappush(l, a+1)
        heappush(l, c+1)
        # print(l, a, c, sum(l))
    # print(sum(l), l)
    print('YES' if sum(l) in {0} else 'NO')


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
