from math import ceil


for i in range(int(input())):
    n = int(input())
    ans = 0
    for i in map(int, input().split()):
        ans += ceil(i/2)
    print(ans)
