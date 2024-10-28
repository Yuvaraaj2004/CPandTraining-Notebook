

from collections import Counter


for t in range(int(input())):
    n, k = list(map(int, input().split()))
    a, b = Counter([i % k for i in map(int, input().split())]), Counter(
        [i % k for i in map(int, input().split())])

    # print(a, b)
    ans = a[0]*b[0]
    for i in a:
        # print(i, k-i, a[i], b[k-i])
        if i != 0:
            ans += a[i]*b[k-i]
    print(ans)
