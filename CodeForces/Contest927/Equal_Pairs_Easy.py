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
    n = II()
    l = GL(rtype=Counter)
    zero = l[0]
    ans, mx, added = 0, 0, 0
    del l[0]
    if l:
        mx = max([((l[i]+zero)*(l[i]+zero-1)//2, i) for i in l])
        del l[mx[1]]
        print(sum(l[i]*(l[i]-1)//2 for i in l)+mx[0])

    else:
        print(zero*(zero-1)//2)
    # print(mx)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
