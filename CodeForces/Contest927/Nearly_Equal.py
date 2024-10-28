for t in range(int(input())):
    a, b = list(map(int, input().split()))
    s1, s2 = input(), input()
    ans = b
    for i in range(a-b+1):
        c = 0
        for j in range(b):
            if s1[i+j] == s2[j]:
                c += 1
        ans = min(ans, b-c)
        # print(i, c)
    print(ans)
