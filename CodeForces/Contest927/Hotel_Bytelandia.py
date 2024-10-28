'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache


mod = 10**9+7


def GetL(type): return map(type, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def Solve():
    n = GetI()
    l = [(i, 1) for i in GetL(int)]+[(i, 0) for i in GetL(int)]
    l.sort()
    ans, o = 0, 0
    for x, y in l:
        if y == 1:
            o += 1
        elif y == 0:
            o -= 1
        ans = max(ans, o)
    print(ans)


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
