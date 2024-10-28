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


@cache
def dp(n):
    if n == 0:
        return False
    elif n < 0:
        return True
    return not dp(n-1) or not dp(n-2)


def Solve():

    print('ALICE' if (II()) == 1 else 'BOB')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
