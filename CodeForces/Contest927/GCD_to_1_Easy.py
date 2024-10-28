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


primes = Seieve(3*10**6)
print(len(primes))


def Solve():
    a, b = M()
    mn = max(a, b)
    for i in range(a):
        print(*[primes[(i+j) % (mn)] for j in range(b)])

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
