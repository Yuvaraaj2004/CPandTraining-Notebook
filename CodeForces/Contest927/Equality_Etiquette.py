'''
Created at: 13-July-24 20:52
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache


mod = 10**9+7


def GetL(): return map(int, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


@cache
def f(n, i=1):
    if n == i:
        return 0
    elif


def Solve(l):
    a, b = GetL()


l, d = [], []

if __name__ == "__main__":
    l = [list(GetL()) for i in range(int(input()))]
    d = [None]*max([abs(x-y)+1 for x, y in l])
    Solve()
