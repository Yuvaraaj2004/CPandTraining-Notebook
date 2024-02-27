from functools import cache


n, nq = map(int, input().split())
arr = list(map(int, input().split()))


@cache
def Find(q):
    l, r = 0, n-1
    # print(q,end=' ')
    while l <= r:
        mid = (l+r)//2
        # print(l,r,arr[mid])
        if arr[mid] == q:
            # print(True)
            return True
        elif arr[mid] < q:
            l = mid+1
        else:
            r = mid-1
    # print(False,l,r)
    return False

print(['YES\n' if Find(i) else 'NO\n' for i in list(map(int, input().split()))]))