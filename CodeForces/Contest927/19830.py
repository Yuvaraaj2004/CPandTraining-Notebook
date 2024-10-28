for t in range(int(input())):
    n = int(input())
    # l = [i for i in range(1, n+1)]
    # for i in range(2, n+1):
    #     for j in range(i, n+1, i):
    #         l[j] *= i
    #     # print(l)
    # l.pop(0)
    # print([i for i in range(1, n+1) if sum(j for j in range(i, n+1, i)) % i != 0])
    l = ([i for i in range(1, n+1)])
    print(*l)
