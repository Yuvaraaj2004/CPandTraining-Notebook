t = int(input())
for t in range(t):
    ans = 0
    a, b = map(int, input().split())
    l1, l2 = sorted(list(map(int, input().split()))), sorted(
        list(map(int, input().split())))
    # print(l1, l2)
    ai, aj, bi, bj = 0, a-1, 0, b-1
    while ai <= aj:
        v = [abs(l1[ai]-l2[bj]), abs(l1[aj]-l2[bi])]
        # print(ai, aj, bi, bj, ans, v)
        if v[0] <= v[1]:
            ans += v[1]
            aj -= 1
            bi += 1
        else:
            ans += v[0]
            ai += 1
            bj -= 1
    print(ans)
