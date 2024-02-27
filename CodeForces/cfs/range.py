n=int(input())
arr=sorted(list(map(int,input().split())))

def upper(q):
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        # print(l,r,arr[mid])
        if arr[mid] <= q:
            l = mid+1
        else:
            r = mid-1
    # print(False,l,r)
    return l+1

def lower(q):
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        # print(l,r,arr[mid])
        if arr[mid] < q:
            l = mid+1
        else:
            r = mid-1
    # print(False,l,r)
    return l+1

def f(x,y):
    return upper(y)-lower(x)


print(*[f(*list(map(int, input().split()))) for i in range(int(input()))])