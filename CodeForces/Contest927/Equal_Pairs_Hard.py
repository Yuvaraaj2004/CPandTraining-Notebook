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
    zero = II()
    q = [GL() for i in range(zero)]
    l, ans = Counter(), []
    cur, sum, mx, added = defaultdict(int), 0, -1, 0
    for x, y in q:
        l[y] += 1
        zero -= 1
        if l[mx] < l[y]:
            ans.append(sum-cur[y]+(zero+l[y])*(zero+l[y]-1)//2)
            sum += (l[y]*(l[y]-1)//2)-cur[y]
            cur[y] = (l[y]*(l[y]-1)//2)
            mx = y
        else:
            sum += (l[y]*(l[y]-1)//2)-cur[y]
            cur[y] = (l[y]*(l[y]-1)//2)
            ans.append((l[mx]+zero)*(l[mx]+zero-1)//2+sum-cur[mx])
        # print(ans, cur, sum, mx)
    print(*ans)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
