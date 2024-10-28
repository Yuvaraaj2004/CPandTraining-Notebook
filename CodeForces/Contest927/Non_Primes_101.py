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


def Seieve(n):
    prime, i = [True] * (n + 1), 2
    l = []
    while i * i <= n:
        if prime[i]:
            l.append(i)
            for j in range(i * i, n + 1, i):
                prime[j] = False
        i += 1
    prime[0] = prime[1] = False
    return prime


prime = Seieve(10**5*2+1)


def Solve():
    n, l = II(), GL()
    p, np, tc, o = [], [], [], []
    for ind, i in enumerate(l):
        if i == 1:
            o.append(ind+1)
        elif i == 2:
            tc.append(ind+1)
        elif prime[i]:
            p.append(ind+1)
        else:
            np.append(ind+1)

    if len(tc) >= 2:
        print(*tc[:2])
        return
    if len(p) >= 2:
        print(*p[:2])
        return
    if len(np) >= 2:
        print(*np[:2])
        return
    if tc:
        for i in p+np:
            if not prime[2+l[i-1]]:
                print(tc[0], i)
                return
    if o:
        for i in p+np:
            if not prime[1+l[i-1]]:
                print(o[0], i)
                return
    if p and np:
        for i in p:
            for j in np:
                if not prime[l[i-1]+l[j-1]]:
                    print(i, j)
                    return
    print(-1)


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
