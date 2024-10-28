# from collections import defaultdict


for t in range(int(input())):
    v = n = int(input())
    l = [i for i in list(map(int, input().split())) if i]
    v = n = len(l)
    c, f, s = 0, False, set()
    while n:
        rm, fg = set(), False
        for ind, i in enumerate(l):
            if i & 1:
                fg = True
                if not f:
                    s |= {ind}
                else:
                    s -= {ind}
            if l[ind] and (l[ind] >> 1) == 0:
                n -= 1
            l[ind] >>= 1

        if not fg:
            f = True
        # print(l, s)
    print(v-len(s))
