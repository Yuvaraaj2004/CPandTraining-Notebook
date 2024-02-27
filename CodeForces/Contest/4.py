test= int(input())
for t in range(test):
    n = int(input())
    l = list(map(int, input().split()))
    q = int(input())
    querys = ([list(map(int, input().split())) for i in range(q)])
    res,j={},0
    for x,y in sorted(q):
        x,y=x-1,y-1