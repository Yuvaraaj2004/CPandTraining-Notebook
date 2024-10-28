'''
Created By: _Cypher_0101
'''


import itertools
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


def c(l):
    v = [(i, ind) for ind, i in enumerate(l)]
    v.sort()
    # print(l, v)
    i, co = 0, 0
    # print(v)
    while i < len(v):
        j = i+1
        while j < len(v) and v[j][1] > v[j-1][1]:
            j += 1
        co += 1
        i = j
    return co


def Solve():
    n = int(input())
    if n == 1:
        print(1)
    elif n & 1:
        print(*(list(range(1, n//2+1))+list((range(n, n//2, -1)))))
    else:
        print(-1)
    pass


if __name__ == "__main__":
    # for j in range(2, 11):
    #     l = []
    #     for i in ((itertools.permutations(list(range(1, j))))):
    #         if ((v := c(i)) == c(i[::-1])):
    #             l.append((i, v))
    #     l.sort()
    #     print(l[0] if l else None)
    # # for i in [[3, 1, 2], [2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 3],
    #           [2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 3]]:
    #     print(c(i), c(i[::-1]))
    for i in range(int(input())):
        Solve()
