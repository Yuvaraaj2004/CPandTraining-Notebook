from collections import Counter


for i in range(int(input())):
    n, x = map(int, input().split())
    l = sorted(map(int, input().split()))
    c = Counter(l)
    k = sorted(c.keys())

    s = 0
    for i in l:
        s += i*2
    for i in range(x):
        q = int(input())
        if q > s-l[0]-l[1] or q < s-l[-1] - l[-2]:
            print(-1)
        elif q == s-l[0]-l[1]:
            print(l[0], *l[2:], l[1])
        else:
            need = s-q
            ans = []
            for i in l:
                if i == need-i:
                    if c.get(i, 0) > 2:
                        ans = [i]*2
                elif c.get(need-i, 0) > 1:
                    ans = [i, need-i]
            if ans:
                c[ans[0]] -= 1
                c[ans[1]] -= 1
                p = []
                for i in k:
                    p += [i]*c[i]
                print(ans[0], *p, ans[1])
                c[ans[1]] += 1
                c[ans[0]] += 1

            # print(s-l[0]-l[1], s, need)
    # print(s)
