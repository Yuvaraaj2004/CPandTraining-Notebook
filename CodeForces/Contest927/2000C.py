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


def GL(type=int): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def Solve():
    n, l, c = II(), GL(), II()
    for i in range(c):
        char, pat, t, f = {}, {}, I(), 0
        if len(t) != n:
            print('NO')
            continue
        for ind, j in enumerate(t):
            if j not in char:
                char[j] = l[ind]
            if l[ind] not in pat:
                pat[l[ind]] = j
            if pat[l[ind]] != j or char[j] != l[ind]:
                # print(pat[l[ind]], char[j], j, l[ind])
                # print(pat, char)
                f = 1
                break
        print('YES' if f == 0 else 'NO')

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
