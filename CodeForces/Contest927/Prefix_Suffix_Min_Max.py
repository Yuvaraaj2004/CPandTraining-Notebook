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


def primeFactors(n):
    l, i = Counter(), 2
    while i*i <= n:
        while n != 1 and n % i == 0:
            l[i] += 1
            n //= i
        i += 1
    if n != 1:
        l[n] += 1
    return l


def Solve():
    print(primeFactors(684/9))


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
