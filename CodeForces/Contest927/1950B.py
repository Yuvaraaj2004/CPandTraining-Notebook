for t in range(int(input())):
    n = int(input())

    for i in range(n):
        print(
            (''.join(['..' if (i+j) & 1 else '##' for j in range(n)])+'\n')*2, end=' ')
