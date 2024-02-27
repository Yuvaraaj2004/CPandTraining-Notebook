t=int(input())
for i in range(t):
    n,s=int(input()),input()
    p,n=0,0
    ans=[]
    for i in s+' ':
        if i=='+':
            if n>0:ans.append(['-',n]);n=0
            p+=1
        elif i=='-':
            if p > 0:
                ans.append(['+', p])
                p = 0
            n+=1
        else:
            ans.append(['+',p] if p else ['-',n])
    pre,s=ans[0][1],0
    v=0
    for i in range(len(ans)-1):
        v+=max(0,ans[i][1]-ans[i+1][1])
        ans[i+1][1]=max(0,ans[i+1][1]-ans[i][1])
    v+=ans[-1][1]
    print(v)