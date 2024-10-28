'''
Created By: _Cypher_0101
'''


from math import gcd, log2, ceil, floor, sqrt
from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def M(type=int): return (map(type, input().split()))


def GL(type=int): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def gcd(x, y): return (y) if x == 0 else gcd(y % x, x)


def Solve():
    n = I()
    l = GL()
    if len(set(l)) == 1:
        print('YES')
    else:
        l = [i for i in l if i != 0]
        l.sort()
        g = l[0]
        for i in l:
            g = gcd(g, i)
        # print(g)
        print('YES' if l[0] == g and all((i//g) & 1 for i in l) else 'NO')

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
