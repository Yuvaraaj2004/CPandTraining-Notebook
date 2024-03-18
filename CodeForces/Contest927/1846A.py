
for i in range(int(input())):
    n, s = int(input()), 0
    for j in range(n):
        a, b = (map(int, input().split()))
        s += a-b > 0
    print(s)


# main()
