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
    a, b, c = GetL(int)
    ans = 0
    for i in range(1, a+1):
        if b*i <= c:
            ans = i
        else:
            break
    print(a-ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
