from math import ceil, floor, sqrt


n=float(input())
l,r=floor(sqrt(n)),ceil(sqrt(n))
f=lambda x:x**2+x**0.5
while r-l>=1e-8:
    mid=(l+r)/2
    v=f(mid)
    # print(l,r,mid,v)
    if v<n:l=mid
    elif v>n:r=mid
print(l)