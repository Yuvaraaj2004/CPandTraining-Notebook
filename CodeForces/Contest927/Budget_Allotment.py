'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappush, heappushpop, heappop

mod = 10**9+7


def GetL(type): return map(type, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def Solve():
    a, b = GetL(int)
    l = sorted(GetL(int), reverse=True)
    tot = 0
    ans = 0
    heap = []
    for i in l:
        if i < b:
            if tot-(b-i) >= 0:
                ans += 1
                tot -= b-i
        elif i >= b:
            ans += 1
            tot += i-b

        # print(heap, ans)
    print(ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
