# cook your dish here
t = int(input())


def f(n, l, k):
    stack = []
    ans = 0
    while l and k > 0:
        s = sum(l[i]*l[0] for i in range(1, len(l)))
        for i in stack:
            s -= i*l[0]
        # print(l[0], ans, k-s)
        if k >= s:
            ans += 1
            k -= s
            stack.append(l.pop(0))
        else:
            break
    return n-ans if ans != n else 1


def g(first, rem, cost):
    if cost >= sum(first*i for i in rem):
        return 1
    else:
        return float('inf')


while t:
    n, k = list(map(int, input().split()))
    first, *l = list(map(int, input().split()))
    l.sort()

    print(min(f(n, sorted([first]+l), k), g(first, l, k)))
    t -= 1
