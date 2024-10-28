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
    l = GL()
    ans = 0
    mx, e = 0, Counter()
    for i in l:
        if i & 1:
            mx = max(mx, i)
        else:
            e[i] += 1
    if mx != 0:
        for k, v in sorted(e.items()):
            if mx < k:
                mx += 2*k*v
                ans += 1+v
            else:
                mx = max(mx, mx+k*v)
                ans += v
            # print(mx, (k, v), ans)

    print(ans)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
