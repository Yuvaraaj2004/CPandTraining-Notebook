'''
Created at: 14-July-24 20:20
Created By: _Cypher_0101
'''


from math import log2, ceil, floor, sqrt
# from sortedcontainers import *
from collections import Counter, defaultdict
from functools import cache


mod = 10**9+7


def GetL(): return map(int, input().split())


def GetS(): return input()


def GetI(): return int(GetS())


def Solve():
    pass


if __name__ == "__main__":
    n = int(input())
    d = {(v := list(map(str, input().split())))[1]: v[0] for i in range(n)}
    for t in range(int(input())):
        a, b = map(str, input().split())
        b = list(b)
        for ind, i in enumerate(b):
            if i in d:
                b[ind] = d[i]
        print('YES' if a == ''.join(b) else 'NO')
