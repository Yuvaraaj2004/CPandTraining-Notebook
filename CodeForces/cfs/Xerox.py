from math import ceil


n,x,y=map(int,input().split())
n+=1
l,r=ceil(n/(x+y)),ceil(n/max(x,y))
while l<r:
    mid=(l+r)//2
    if Valid(mid):
        