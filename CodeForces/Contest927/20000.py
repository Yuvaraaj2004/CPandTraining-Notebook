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
    s = I()
    # print(s[:2], s[2] != '0', int(s[2:]))
    print('YES'if len(s) > 2 and s[:2] == '10' and s[2]
          != '0' and int(s[2:]) >= 2 else 'NO')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
