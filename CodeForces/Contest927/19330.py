for i in range(int(input())):
    n = int(input())
    print(sum(abs(i) for i in list(map(int, input().split()))))
