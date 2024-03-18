t=int(input())
for t in range(t):
    n,c,a,b=(map(int,input().split()))
    l=[0]+list(map(int,input().split()))
    f=0
    for i in range(1,n+1):
        c-=min((l[i]-l[i-1])*a,b)
        if c <= 0:
            f=1
            print('NO')
            break
    if f==0: print('YES')
