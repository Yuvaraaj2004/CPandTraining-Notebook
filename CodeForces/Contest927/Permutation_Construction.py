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
    n = II()
    if n == 1:
        print(1)
    elif n == 2:
        print(1, 2)
    elif n == 3:
        print(1, 3, 2)
    elif n == 4:
        print(1, 4, 2, 3)
    else:
        l = [list(range(1, ceil(n/2)+1)), list(range(ceil(n/2)+1, n+1))]
        ans = []
        while l[0]:
            ans.append(l[0].pop(0))
            if l[1]:
                ans.append(l[1].pop(0))
        print(*ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
