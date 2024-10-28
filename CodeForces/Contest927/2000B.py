'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush

# from sortedcontainers import SortedList


mod = 10**9+7


def M(type=int): return (map(type, input().split()))


def GL(type=int): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():

    n = II()
    f = 0
    l, r = None, None
    for i in GL():
        if l is None:
            l = r = i
        else:
            if i == l-1:
                l -= 1
            elif i == r+1:
                r += 1
            else:
                f = 1
                break
    print('NO' if f == 1 else 'YES')


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
