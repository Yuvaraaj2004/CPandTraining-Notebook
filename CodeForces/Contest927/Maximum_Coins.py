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
    a, b = GetL(int)
    ans = 0
    for i in range(a, 0, -1):
        ans += (1 << i)*(-1 if i <= a-b else 1)
        # print(ans)
    print(ans)
    # pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
