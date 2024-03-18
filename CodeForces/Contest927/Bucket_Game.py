from math import ceil


for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)-n
    turn = s & 1
    s = [0, 0]
    for i in range(n):
        s[turn] += 1
        turn = not turn
    print(s)
