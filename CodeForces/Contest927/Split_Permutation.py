for t in range(int(input())):
    n = int(input())
    l = [[n]]
    i, j = 1, n-1
    while i < j:
        l .append([i, j])
        i += 1
        j -= 1
    extra = []
    while len(l) > 2:
        nl = []
        while l:
            if len(l) >= 2:
                nl.append(l.pop(0)+(l.pop(0)))
            else:
                extra.append(l.pop(0))
        l = nl
    # print(l+extra)

    if i == j:
        l.append([j])
    ans = []
    for i in l:
        ans += i
    print(*ans)
