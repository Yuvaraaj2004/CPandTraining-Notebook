def f(n, l):
    for i in range(n-2, -2, -1):
        if i-1 >= 0:
            l[i-1] -= (l[i])//2
            if l[i-1] < 0:
                return False
        if i+1 < n:
            l[i+1] -= (l[i])//2
            if l[i+1] < 0:
                return False
        l[i] -= (l[i])//2*2
        if l[i] < 0:
            return False
    # print(l)
    return (1 if sum(i == 0 for i in l) == n else 0)


def main():
    for i in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        print('YES' if f(n, l[::]) or f(n, l[::-1]) else 'NO')


if __name__ == "__main__":
    main()
