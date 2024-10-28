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
    ans = 0
    for i in GL():
        if i <= b:
            b -= i
        else:
            break
        ans += 1
    print(ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
