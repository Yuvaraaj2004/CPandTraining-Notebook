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

    a, b = GL()
    s1, s2 = list(I()), list(I())

    def f(s1, s2):
        changed, l = [], 0
        ans = []
        for i in range(a-b+1):
            if (changed and changed[-1][0] != s2[i]) or (not changed and s1[i] != s2[i]):
                # if changed:
                #     print(changed[-1][0], s2[i], changed[-1][0] != s2[i])
                changed.append((s2[i], i))
            if changed and changed[0][1] <= i-b:
                ans.append(changed.pop(0))
            # print(changed, ans)
        f = 1
        for i in range(a-b+1, a):
            if changed and changed[-1][1]-i <= b and changed[-1][0] != s2[i]:
                f = -1
            elif not changed and s1[i] != s2[i]:
                f = -1
        if len(ans)+len(changed) > a//2:
            f = -1
        return f, ans+changed
    l = [f(s1, s2), f(s1[::], s2[::])]
    l.sort(key=lambda x: (-x[0], len(x[1])))
    # print(l)
    if l[0][0] == -1:
        print(-1)
    else:
        ans = l[0][1]
        print(len(ans))
        for i in ans:
            print(f'{i[1]+1} {i[0]}')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
