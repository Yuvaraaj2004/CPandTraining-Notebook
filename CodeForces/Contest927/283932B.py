n,k=map(int,input().split())
a=[int(input()) for i in range(n)]

def  Check(mid):
    return sum(i//mid for i in a)>=k


l,r=1,sum(a)
while r-l>1e-6:
    mid=(l+r)/2
    # print(l, r, mid, (v := Check(mid)))
    if (v := Check(mid)):
        l=mid
    else:
        r=mid
print(f"{round(r,6)}")