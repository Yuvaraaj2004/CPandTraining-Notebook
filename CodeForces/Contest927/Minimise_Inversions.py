'''
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache


mod = 10**9+7


def GetL(type): return map(type, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def f(s):
    i, o,  ans = 0, 0,  0
    while i < len(s):
        if s[i] == '1':
            o += 1
        elif s[i] == '0':
            ans += o
        i += 1
    print(''.join(s), ans)
    return ans


def Solve():
    a, b = GetL(int)
    s = list(GetS())

    @cache
    def f(ind=0, c=0, k=b):
        print(locals())
        if ind == len(s):
            return 0
        if s[ind] == '0':
            v = min(f(ind+1, c, b)+c, (f(ind+1, c+1, b-1) if b else float('inf')))
            # print(ind, v)
            return v
        else:
            v = min(f(ind+1, c+1, b), (f(ind+1, c, b-1)+c if b else float('inf')))
            # print(ind, v)
            return v

    print(f())

    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
