for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print('YES' if len(l) != 2 or sorted(l) == l else 'NO')
