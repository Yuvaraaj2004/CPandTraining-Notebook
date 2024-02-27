t = int(input())
for t in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    i, j = 0, n-1
    while i < len(l) and l[i] == 0:
        i += 1
    while i < len(l) and l[i] == 1:
        i += 1
    print(sum(l[i:]))
