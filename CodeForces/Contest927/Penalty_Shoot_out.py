for t in range(int(input())):
    a, b = list(map(int, input().split()))
    f = 0
    for i in range(3):
        for j in range(2):
            if a+i == b+j:
                f = 1
    print('YES' if f == 1 else 'NO')
