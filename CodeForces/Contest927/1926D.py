# from collections import Counter

mask = (1 << 31)-1
for i in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    # print(mask)
    ans = 0
    s = {}
    for j in c:
        if s.get(mask ^ j, 0) > 0:
            s[mask ^ j] -= 1
        else:
            ans += 1
            s[j] = s.get(j, 0)+1
    print(ans)
