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
    a, b = list(I()), (I())
    l = 0
    for ind, i in enumerate(a):
        if i == '?':
            a[ind] = b[l] if l < len(b) else 'a'
            l += 1
        elif l < len(b) and i == b[l]:
            l += 1
        # print(a)

    print('YES\n'+''.join(a) if l >= len(b) else 'NO')

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
