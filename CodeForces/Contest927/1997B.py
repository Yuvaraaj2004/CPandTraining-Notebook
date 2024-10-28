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
    n = GetI()
    a = [GetS(), GetS()]
    ans = 0
    for i in range(2):
        for j in range(1, n-1):
            if a[i][j] == '.' and a[i][j-1] == '.' and a[i][j+1] == '.' and a[not i][j-1] == 'x' and a[not i][j+1] == 'x' and a[not i][j] == '.':
                ans += 1
                # print(i, j)
            # print(a[i][j] == '.', a[i][j-1] == '.', a[i][j+1] ==
                #   '.', a[not i][j-1] == 'x', a[not i][j+1] == 'x')
    print(ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
