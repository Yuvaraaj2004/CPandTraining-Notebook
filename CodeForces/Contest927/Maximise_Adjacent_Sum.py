for i in range(int(input())):
    n = int(input())
    l = sorted(map(int, input().split()))
    ans = l[0]+l[1]
    for i in range(2, len(l)):
        ans += l[i]*2
    print(ans)
