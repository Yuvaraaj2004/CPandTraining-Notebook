from math import ceil


t=int(input())
for i in range(t):
    n=int(input())
    print((n//2)-(n&1==0))