# cook your dish here
t = int(input())
while t:
    n = int(input())
    l = list(range(1, n+1))
    print(*l)
    print(*l[len(l)//2:], *l[:len(l)//2])
    t -= 1
