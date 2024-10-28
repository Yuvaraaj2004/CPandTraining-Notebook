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


d = [0]*(int(2e5)+1)


def f(x):
    if x <= 2:
        return 1
    else:
        return f(x//3)+1


for i in range(1, len(d)):
    if i <= 2:
        d[i] = 1
    else:
        d[i] = d[i//3]+1
for i in range(1, len(d)):
    d[i] += d[i-1]
# print(d)


def Solve():
    a, b = M()
    print(d[b]-d[a-1]+d[a]-d[a-1])
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
