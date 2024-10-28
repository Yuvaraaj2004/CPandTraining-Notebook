'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def GetL(type): return map(type, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def Solve():
    n, s = GetI(), list(GetS())
    ans, l = 0, []
    for i in range(n):
        if len(l) == 0 and s[i] == '_' or s[i] == '(':
            s[i] = "("
            l.append(i)
        else:
            s[i] = ")"
            ans += i-l.pop()

    print(ans)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
