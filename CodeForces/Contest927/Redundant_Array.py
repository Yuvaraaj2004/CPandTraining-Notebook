from collections import Counter
for t in range(int(input())):

    n, c = int(input()), Counter(list(map(int, input().split())))
    ans = float('inf')
    for i in c:
        ans = min(ans, (n-c[i])*i)
    print(ans)
