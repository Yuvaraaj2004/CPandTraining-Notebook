'''
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
    n, k = GetL()
    l, ans = [[], []], [0, 0]
    for ind, i in enumerate(GetL()):
        l[ind & 1].append(i)
        ans[ind & 1] += i
    l[0].sort(), l[1].sort()
    print(l, ans)
    while l[0] and l[1] and l[0][-1] >= l[1][0] and k:
        if l[0][-1] == l[1][0]:
            while l[1] and l[0][-1] == l[1][0]:
                l[1].pop(0)
            print(l)
        else:
            ans[1] += l[0][-1]-l[1][0]
            ans[0] -= l[0][-1]-l[1][0]
            print(l[0][-1]-l[1][0], ans, l)
            l[0].pop(), l[1].pop(0)
            # print(l, ans)
            k -= 1
    print('YES' if ans[0] < ans[1] else 'NO')
    pass


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
