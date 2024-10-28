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
    a, b = M()
    lis = GL()
    sufa, sufb = [0, 0], [0, 0]
    for ind, i in enumerate(lis):
        ind += 1
        if i == 1:
            sufa[0] += ind
            sufa[1] += 1
        elif i == 2:
            sufb[0] += ind
            sufb[1] += 1
        elif i == 3:
            sufa[0] += ind
            sufa[1] += 1
            sufb[0] += ind
            sufb[1] += 1
    print(sufa, sufb)
    prea, preb = [0, 0], [0, 0]
    ans = []
    for ind, i in enumerate(lis):
        ind += 1
        v = ((sufa[0], sufa[1]*ind, prea[1]*ind, prea[0]),
             (sufb[0], sufa[1]*ind, prea[1]*ind, prea[0]))
        ans.append(abs((sufa[0]-sufa[1]*ind+prea[1]*ind-prea[0]) -
                   (sufb[0]-sufa[1]*ind+prea[1]*ind-prea[0])))
        if i == 1:
            prea[0] += ind
            sufa[0] -= ind
            sufa[1] -= 1
            prea[1] += 1
        elif i == 2:
            sufb[0] -= ind
            preb[0] += ind
            sufb[1] -= 1
            preb[1] += 1
        elif i == 3:
            prea[0] += ind
            prea[1] += 1
            preb[0] += ind
            preb[1] += 1
            sufa[0] -= ind
            sufa[1] -= 1
            sufb[1] -= 1
            preb[1] += 1
        print(ind, prea, preb, v)
    # prea, preb = [0, 0], [0, 0]
    print(ans)
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
