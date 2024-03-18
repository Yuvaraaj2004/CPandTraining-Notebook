for i in range(int(input())):
    n, *l = map(int, input().split())
    s = n % sum(l)
    # print(s)
    print('Alice' if s <= l[0] and s != 0 else 'Bob')

    # print('Alice' if dp() else 'Bob')
