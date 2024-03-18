def main():
    for i in range(int(input())):
        n = int(input())
        l = sorted((map(int, input().split())))
        ans, mn = 0, float('inf')
        for j in range(n-1, -1, -1):
            mn = min(l[j], mn)
            ans = max(ans, mn*(n-j))
        print(ans)


if __name__ == "__main__":
    main()
