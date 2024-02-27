from collections import Counter


t=int(input())
for t in range(t):
    a,b=map(int,input().split())
    c = Counter(tuple(map(int, input().split()))for i in range(b))
    l,sweep = list(c.keys()),[]
    for ind,(x,y) in enumerate(l):
        sweep.append((x,0,ind))
        sweep.append((y,1,ind))
    sweep.sort()
    # print(sweep)
    s,ind,ans=0,set(),0
    r=[]
    for (x,y,z) in sweep:
        if y==0:
            s+=c[l[z]]
            ind.add(z)
        else:
            s-=c[l[z]]
            ind.discard(z)
        ans=max(ans,s)
        print(ind,ans)
        if len(ind)==0:
            r.append(ans)
            ans=0
    print(sum(r))

    print(l)