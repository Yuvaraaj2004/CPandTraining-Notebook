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
    a, b, c = M()
    if a*b <= c*c:
        return 0
    elif a <= c*c or b <= c*c:
        return 1
    else:
        return 2
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        print(Solve())
