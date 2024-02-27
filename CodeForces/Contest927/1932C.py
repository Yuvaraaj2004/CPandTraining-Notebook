t=int(input())
for test in range(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=input()
    lef,rig=0,a-1
    for i in s[:-1]:
        if i=='L':lef+=1
        if i=='R':rig-=1
        if lef==rig:break
    ans=[l[lef]%b]
    
    for i in s[-2::-1]:
        if i=='R':
            rig+=1
            ans.append(l[rig]*ans[-1]%b)
        elif i=='L':
            lef-=1
            ans.append(l[lef]*ans[-1]%b)
    print(*(ans[::-1]))

