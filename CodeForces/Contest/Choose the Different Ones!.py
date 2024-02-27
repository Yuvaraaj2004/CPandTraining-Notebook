t=int(input())
for i in range(t):
    # print(i)
    a,b,v=map(int,input().split())
    l1,l2=sorted(set(map(int,input().split()))),sorted(set(map(int,input().split())))
    c1,c2,i,j=0,0,0,0
    s=set()
    for k in range(1,v+1):
        f=False
        if i < len(l1) and l1[i] == k:
            c1+=1;i+=1
            f=True
            while i<len(l1) and  l1[i]==k:
                i+=1
        if j<len(l2) and l2[j]==k:
            c2+=1;j+=1
            f=True
            while j<len(l2) and l2[j]==k:
                j+=1
        if not f:
            c1,c2=0,0
            break
        s.add(k)
    # print(s)
    print ('YES'if c1>=v//2 and c2>=v//2 and len(s)==k else 'NO')