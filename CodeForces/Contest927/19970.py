'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache
from heapq import heapify, heappop, heappush


mod = 10**9+7


def GetL(type): return map(type, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def Solve():
    s = GetS()
    c, i = [0, None], 0
    while i < len(s):
        j = i+1
        while j < len(s) and s[j] == s[i]:
            j += 1
        if c[0] < j-i-1:
            c[0] = j-i-1
            c[1] = i
        i = j

    l = list(s)
    if c[1] != None:
        l.insert(c[1]+1, chr((ord(s[c[1]])-ord('a')+1) % 26+ord('a')))
    else:
        l.insert(0, chr((ord(s[0])-ord('a')+1) % 26+ord('a')))

    print(''.join(l))

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
