'''
Created at: 28-August-24 09:30
Created By: _Cypher_0101
'''

from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from typing import *
from heapq import heapify, heappop, heappush


mod = 10**9+7
def gcd(x, y): return (y) if x == 0 else gcd(y % x, x)


def Seieve(n):
    prime, i = [True] * (n + 1), 2
    l = []
    while i * i <= n:
        if prime[i]:
            l.append(i)
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1
    return [ind for ind, i in enumerate(prime) if i][2:]


def getBits(n):
    c, l = 0, []
    while n:
        if n & 1:
            l.append(c)
        n >>= 1
        c += 1
    return l


def exists(nums):
    return lambda x, y: x >= 0 and y >= 0 and x < len(nums) and y < len(nums[i])


def BE(b, e, mod=mod):
    b %= mod
    res = 1
    while e:
        if e & 1:
            res = (res * b) % mod
        b = (b * b) % mod
        e >>= 1
    return res


@cache
def fact(n): return 1 if n <= 1 else (n * fact(n - 1) % mod)


def M(type): return (map(type, input().split()))


def GL(type): return list(map(type, input().split()))


def I(): return input()


def II(): return int(I())


def p(*args): print(*args)


@cache
def check(arr, rooms):
    heap = [0]*rooms
    for x, y in arr:
        mn = heappop(heap)
        if mn > x:
            return False
        heappush(heap, y)
        # print(heap)
    return True


def Solve(arr):
    arr = tuple(tuple(i) for i in (sorted(arr, key=lambda x: x[0])))
    print(arr)
    l, r, ans = 1, len(arr), len(arr)
    while l < r:
        mid = (l+r)//2
        print(mid, check(arr, mid))
        if check(arr, mid):
            ans = mid
            r = mid
        else:
            l = mid+1
    print(ans, l, r)


if __name__ == "__main__":
    for i in [[[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]], [[0, 30], [5, 10], [15, 20]]]:
        Solve(i)
