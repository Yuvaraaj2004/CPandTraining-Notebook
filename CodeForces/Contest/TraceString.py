from collections import defaultdict


t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d=defaultdict(list)
    char=97
    ans=[]
    for ind,i in enumerate(l):
        if i==0:
            d[0].append(chr(char))
            ans.append(chr(char))
            char+=1
        else:
            val=d[i-1].pop(0)
            ans.append(val)
            d[i].append(val)
    print(''.join(ans))
