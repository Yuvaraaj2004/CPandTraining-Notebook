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
    n, l = II(), GL(rtype=sorted)

    def f(n1, n2):
        # print(n1, n2, n1+n2-1, n2-n1)
        return [n2-n1+1, n1+n2]

    ans = []
    for i in range(n-1):

        s = f(l[i], l[i+1])
        # print(l[i], l[i+1], s)
        ans += [s]
    ans.sort()
    s = 0
    i = 0
    while i < len(ans):
        j = i+1
        while j < len(ans) and ans[j][0] <= ans[i][1]:
            ans[i][1] = max(ans[i][1], ans[j][1])
            j += 1
        # print(ans[i:j])
        s += ans[i][1]-ans[i][0]
        i = j
    print(s)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
