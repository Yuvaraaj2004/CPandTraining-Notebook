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
    n, l = II(), GL()
    s, posmn, neg, negmn = 0, float('inf'), 0, -float('inf')
    negc = 0
    zero = False
    for i in l:
        if i == 0:
            zero = True
        elif i > 0:
            posmn = min(posmn, i)
            s += i
        elif i < 0:
            negmn = max(negmn, i)
            neg -= i
            negc += 1
    print(s, posmn, neg, negmn, negc, zero)
    s += neg

    if negc % 2:
        s -= (-negmn*2 if posmn > -
              negmn else (posmn if posmn != float('inf') else 0)+negmn)

    print(s)
    pass


if __name__ == "__main__":

    for i in range(int(input())):
        Solve()
