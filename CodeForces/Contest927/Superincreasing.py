def f(n):
    global l, fib, s
    for i in range(l, n+1):
        fib[i] = (s+1)
        s += fib[i]
        l += 1
    print(fib[:n+1])
    return fib[n-1]


l, fib, s = 1, [1]+[0]*10**5, 1

for t in range(int(input())):
    a, b, c = list(map(int, input().split()))
    print('YES' if f(b) <= c else 'NO')
