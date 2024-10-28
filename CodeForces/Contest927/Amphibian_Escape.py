from math import ceil


for t in range(int(input())):
    a, b, c = list(map(int, input().split()))
    mn, ans = ceil(b/c), 0
    if (a-c+1) > 0:
        ans += (a-c+1)*a
        a -= c
    for i in range(1, a):
        ans += a-(i+mn)
        print(i, a-i+mn-1)
    print(ans)
    print()
