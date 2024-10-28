for t in range(int(input())):
    n = int(input())
    l = sorted(map(int, input().split()))
    # print(l)
    while l:
        if l[-1] <= n:
            l.pop()
        else:
            break
        n -= 1
    print('NO' if l else 'YES')
