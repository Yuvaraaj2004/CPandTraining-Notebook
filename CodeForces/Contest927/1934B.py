from functools import cache


d = {}
coins = [15, 10, 6, 3]
coins.reverse()


# def dp(n):
#     print(n, end=' ')
#     if n <= 2:
#         return n

#     elif d.get(n, -1) != -1:
#         return d[n]
#     else:
#         ans = n
#         for i in coins:
#             if i > n:
#                 break
#             ans = min(dp(n % i) + n//i, ans)
#         d[n] = ans
#         return ans


def coin(n):
    # print(n, end=' ')
    if n < 3:
        return n
    if n in v:
        return v[n]
    ans = n
    for i in coins:
        # for i in coins:
        if i > n:
            break
        ans = min(coin(n-i)+1, ans)
    v[n] = ans
    return ans


v, d = {}, {}
for i in range(15):
    print(i, coin(i))
