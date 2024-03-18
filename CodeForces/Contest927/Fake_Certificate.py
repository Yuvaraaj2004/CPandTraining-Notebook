for i in range(int(input())):
    n, s = int(input()), input()
    ans, i, prev = 0, 0, 0
    while i < n:
        sum = 0
        while i < n and s[i] == '1':
            sum += 1
            i += 1
        ans = max(ans, prev+sum)
        while i < n and s[i] == '0':
            sum += 1
            i += 1
        prev = sum
    ans = max(ans, prev)
    print(ans)
