for t in range(int(input())):
    a, b = list(map(int, input().split()))
    a, b = a-b, 0
    if a-b >= 10:
        print(0)
    else:
        v = 0
        while a-b < 10:
            a += 3
            # b += 2
            v += 1
            # print(a, b)
        print(v)
