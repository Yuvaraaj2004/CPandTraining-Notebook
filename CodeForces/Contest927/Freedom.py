for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[j]*2 == l[i]*l[j]-l[i]-l[j]:
                ans += 1
    print(ans)
