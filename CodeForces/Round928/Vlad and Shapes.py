from collections import Counter


t = int(input())
for i in range(t):
    n = int(input())
    s = [Counter(input()).get('1', 0) for i in range(n)]
    for i in range(1, n):
        if s[i] and s[i] == s[i-1]:
            print('SQUARE')
            break
        elif s[i] and s[i-1] and abs(s[i]-s[i-1]) == 2:
            print('TRIANGLE')
            break
