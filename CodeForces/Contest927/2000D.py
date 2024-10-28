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
    n = int(input())
    l, s = GL(), I()
    su = sum(l)
    i = 0
    while i < n and s[i] == 'R':
        su -= l[i]
        i += 1
    j = n-1
    while j > i and s[j] == 'L':
        su -= l[j]
        j -= 1
    print(su)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
