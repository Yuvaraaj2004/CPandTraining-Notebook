w, h, n = map(int, input().split())
l, r = h, w*n
# print(l, r)
while l < r:
    mid = (l+r)//2
    # print((mid//w)*(mid//h),l,r)
    if (mid//w)*(mid//h) >= n:
        r = mid
    else:
        l = mid+1
if (l//w)*(l//h) >= n:print(l)
else:print(r)