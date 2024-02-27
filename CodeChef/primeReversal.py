t=int(input())
for  i in range(t):
    a,b=map(int,input().split())
    d=a//b
    print(*[d*i for i in range(1,b+1)])