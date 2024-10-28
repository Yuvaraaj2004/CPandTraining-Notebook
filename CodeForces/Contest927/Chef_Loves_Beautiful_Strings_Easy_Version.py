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
    n, s = II(), I()
    d, i = [[], []], 0
    while i < len(s):
        j = i+1
        while j < len(s) and s[j] == s[i]:
            j += 1
        heappush(d[int(s[i])], -(j-i))
        i = j
    c = len(d[0])+len(d[1])-1
    # print(d)
    ans = 0
    while d[0] and d[1] and d[0][0] != -1:
        heappush(d[0], heappop(d[0])+1)
        # print(d[0])
        ans += c
    while d[0] and d[1] and d[1][0] != -1:
        heappush(d[1], heappop(d[1])+1)
        # print(d[1])
        ans += c
    # print(d)
    if len(d[0]) < len(d[1]):
        d[0], d[1] = d[1], d[0]
    for i in range(len(d[0])):
        d[0].pop()
        if d[0] and d[0]:
            ans += len(d[0])+len(d[1])-1
        if len(d[1]):
            d[1].pop(0)
            if d[1] and d[0]:
                ans += len(d[0])+len(d[1])-1
    print(ans)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
