from collections import Counter


for t in range(int(input())):
    n = int(input())
    c = Counter(map(int, input().split()))
    mn = min(c.keys())
    if c[mn] == 1:
        print('YES')
    else:
        if mn == 1:
            print('NO')
        else:
            k, f = sorted(c.keys()), False
            # print(k)
            for i in range(1, len(k)):
                if k[i] % k[0] != 0 and k[i] % k[0] < mn:
                    f = True
                    break
            print('YES' if f else "NO")
