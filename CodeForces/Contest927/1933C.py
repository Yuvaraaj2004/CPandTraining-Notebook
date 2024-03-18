for i in range(int(input())):
    a, b, l = map(int, input().split())
    v1 = 1
    ans = set()
    while v1 <= l:
        v2 = 1
        while v1*v2 <= l and l % (v1*v2) == 0:

            ans.add(v1*v2)
            v2 *= b
        v1 *= a
    print(len(ans))
