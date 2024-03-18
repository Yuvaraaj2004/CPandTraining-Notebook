for i in range(int(input())):
    a, b, k = map(int, input().split())
    l = [input() for i in range(a)]
    # print(d)
    k += 1

    def dp(l):
        d = [[[0]*k for i in range(b+1)], [[0]*k for i in range(b+1)]]
        ans = 0
        for i in range(a):
            for j in range(b-1, -1, -1):
                c = 0
                for xc, yc in (0, 0), (1, 1), (0, 1):
                    for ind, m in enumerate(d[xc][yc+j]):
                        if ind == k-1:
                            break
                        d[1][j][ind+1] += m
                        c += m
                if l[i][j] == '#':
                    d[1][j][0] = 1
                    c += 1
                else:
                    d[1][j][0] = 0

                ans = max(ans, c)
            # print(d)
            d[0], d[1] = d[1], d[0]
        print(ans)
    dp(l)
