from collections import Counter


t=int(input())
for i in range(t):
    print(max(Counter(input()).items(), key=lambda x:x[1])[0])