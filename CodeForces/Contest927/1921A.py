t=int(input())
for t in range(t):
    d={}
    for i in range(4):
        a,b=map(int,input().split())
        d[a]=d.get(a,[])+[b]
    x=list(d.keys())
    # print(x)
    print(abs(x[1]-x[0])*abs(d[x[1]][0]-d[x[1]][1]))