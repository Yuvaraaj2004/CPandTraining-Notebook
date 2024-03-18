for i in range(int(input())):
    n = int(input())
    d = {}
    l = list(map(int, input().split()))
    for i in l:
        d[i % 3] = d.get(i % 3, 0)+1
    v = d.get(1, 0)*1+d.get(2, 0)*2
    # print(v, d, end=' ')
    if v % 3 != 0:
        if v % 3 == 2:
            if d.get(2, 0) >= 1:
                print(1)
            elif d.get(1, 0) >= 2:
                print(1)
        elif v % 3 == 1:
            if d.get(1, 0) >= 1:
                print(1)
            elif d.get(2, 0) >= 2:
                print(2)
    else:
        print(0)
