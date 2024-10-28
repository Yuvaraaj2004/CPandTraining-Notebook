'''
Created By: _Cypher_0101
'''


from bisect import bisect_left
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
    n, l = II(), GL()
    lis, last = [[]], [[], []]
    for i in l:
        pos1 = bisect_left(last[1], -i)
        if pos1 > len(lis):
            lis.append((lis[pos1*2] if lis else [])+[-i])
            last[0].append(i)
        else:
            lis[i] = lis[pos1*2]+[-i]

        pos2 = bisect_left(last[0], i)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
