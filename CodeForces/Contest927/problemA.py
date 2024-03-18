a, b = map(int, input().split())
ans, r, c = 0, 0, 0
for i in range(a):
    l = input()
    for j in range(b):
        if l[j] != '.' and ans < int(l[j]):
            ans = int(l[j])
            r, c = i, j
print(r+1, c+1)
