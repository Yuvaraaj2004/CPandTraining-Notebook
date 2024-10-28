for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print('YES' if max(l[0], l[-1]) <= min(l) else 'NO')
