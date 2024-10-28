from collections import defaultdict, deque


def RoundRobin(process, tq=2):
    process.sort(key=lambda x: (x[0], x[1], x[2]))
    q, t = deque(), 0
    ans = []
    while process or q:
        if process and t <= process[0][0]:
            while process and t <= process[0][0]:
                # ans.append((t, 'idle'))
                at, id, bt = process.pop(0)
                q.append((bt, id))
                continue
        else:
            BT, id = q.popleft()
            ans.append((t, id, BT-tq, tq if BT >= tq else BT))
            t += tq if BT >= tq else BT
            BT -= tq
            if BT > 0:
                q.append((BT, id))
        print(process, q, t)
    print(ans)


v = 20

l = defaultdict(lambda: [0 for i in range(v)])


def f(l, u, d):
    u = u//d*d
    for i in range(u, l-1, -d):
        if str(i) == str(i)[::-1]:
            print(i, d, len(str(l)), i//d, i//d % 11)
            return i


for i in range(1, 10):
    for n in range(1, v):
        if i == 1 or i == 3 or i == 9:
            l[i][n-1] = ('9'*n)
        elif i == 2:
            l[i][n-1] = ('8'+('' if n < 2 else '9'*(n-2)+'8'))
        elif i == 5:
            l[i][n-1] = ('5'+('' if n < 2 else '9'*(n-2)+'5'))
        elif i == 8 or i == 4:
            l[i][n-1] = '8'*n if n < 4 else '88'+'9'*(n-4)+'88'
        elif i == 6:
            def g(n, f=False):
                if not f and n <= 2:
                    return '6'*n
                if not f and n == 3:
                    return '888'
                if f:
                    if n == 2:
                        return '77'
                    elif n == 3:
                        return '989'
                    else:
                        return '9'+g(n-2, True)+'9'
                else:
                    return '8'+g(n, True)+'8'
            l[i][n-1] = g(n)
        else:
            l[i][n-1] = (f(10**(n-1), (10**n), i))

print(l)
