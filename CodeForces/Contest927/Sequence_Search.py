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
    a, b, k = M()
    s = [0, a, b]
    for i in range(4, k+1):
        s.append(s[-1]+s[-2]-s[-3])
    # print(s)
    if k == 1:
        print(0)
    elif a < b:
        print(b+max(k-2, 0)//2*b if k % 2 == 1 else a+max(k-2, 0)//2*b)
    else:
        l, r = min(a, b), max(b, a)
        diff = b
        for i in range(3, k+1):
            if l < r:
                l += diff
            else:
                r += diff
            # print(i, l, r)
        print(min(l, r))


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
