# from functools import cache


n, nq = map(int, input().split())
arr = list(map(int, input().split()))


def Find(q):
    l, r = 0, n-1
    # print(q,end=' ')
    while l <= r:
        mid = (l+r)//2
        # print(l,r,arr[mid])
        if arr[mid] < q:
            l = mid+1
        else:
            r = mid-1
    # print(False,l,r)
    return l+1


for i in ([Find(i) for i in list(map(int, input().split()))]):
    print(i)
