for t in range(int(input())):
    n = int(input())
    l, ans = input(), []
    for i in range(0, n, 2):
        if int(l[i]) ^ int(l[i+1]):
            ans.append(i+1)
    print(len(ans))
    if ans:
        print(*ans)
