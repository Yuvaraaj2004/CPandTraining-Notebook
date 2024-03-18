for t in range(int(input())):
    x, y = list(map(int, input().split()))
    s = list(input())
    i = 0
    while i < len(s) and y:
        if y and s[i] == '1':
            s.pop(i)
            y -= 1
        else:
            i += 1
    while y:
        s.pop()
        y -= 1
    print(''.join(s[:]))
