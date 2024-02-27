

t=int(input())
def f(n):
    res=0
    while n:
        res+=n%10
        n//=10
    return res
l=[0]*((10**5)*2+1)
for i in range(len(l)):
    l[i]=l[i-1]+f(i)
for i in range(t):
    print(l[int(input())])