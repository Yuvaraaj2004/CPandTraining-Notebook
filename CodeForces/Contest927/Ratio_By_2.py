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
    l = sorted(M())
    if l[1] >= l[0]*2:
        ans = 0
    elif l[1] & 1 == 0:
        ans = (abs(l[1]//2-l[0]))
    else:
        ans = 1+min(abs(l[1]//2-l[0]), abs((l[1]+1)//2-l[0]))
    print(ans)


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
