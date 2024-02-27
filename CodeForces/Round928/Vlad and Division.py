from collections import Counter

mx=(1<<31)-1
# print(len(bin(mx)[2:]))
t = int(input())
for i in range(t):
    n=int(input())
    ans=0
    l,visited=Counter(map(int,input().split())),set()
    for i in l:
        if i in visited:continue
        v=i^mx
        # print(i,v)
        if l.get(v,0):
            mn=min(l.get(i,0),l.get(v,0))
            ans+=mn+(l[i]-mn)+(l[v]-mn)
        else:
            ans+=l.get(i)
        visited.add(i)
        visited.add(v)

    print(ans)
