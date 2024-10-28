'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def M(type): return (map(type, input().split()))


def GL(type): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    n, s = II(), I()
    i, z, o = 0, 0, 0
    while i < len(s):
        while i+1 < len(s) and s[i] == s[i+1]:
            i += 1
        if s[i] == '0':
            z += 1
        else:
            o += 1
        # print(z, o)
        i += 1
    if not o:
        print(n)
    elif not z:
        print(0)
    else:
        ans = 0
        if s[0] == '0' or s[-1] == '0':
            if s[0] == '0':
                i = 0
                while i < len(s) and s[i] == '0':
                    i += 1
                ans = i
                # print(i)
            if s[-1] == '0':
                i = len(s)-1
                while i >= 0 and s[i] == '0':
                    i -= 1
                # print(len(s)-i)
                ans = min(ans, len(s)-i)
        else:
            ans = sum(1 for i in s if i == '0')
        print(ans)

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
