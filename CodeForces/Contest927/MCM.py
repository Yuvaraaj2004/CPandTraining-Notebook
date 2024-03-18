from functools import cache


l = '''2
2
18 19
3
40 60 20
'''.split('\n')
for i in range(int(l.pop(0))):
    n = int(l.pop(0))
    mat = list(map(int, l.pop(0).split()))

    @cache
    def MCM(l=0, r=len(mat)-1):
        # print(l, r)
        if r-l <= 1:
            return mat[l]*mat[r]
        else:
            ans = float('inf')
            for i in range(l+1, r):
                ans = min(ans, MCM(l, i)+MCM(i, r)+mat[l]*mat[r]*mat[i])
            return ans

    print(MCM())
