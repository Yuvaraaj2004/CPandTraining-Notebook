mod = 10**9+7


def main():
    for i in range(int(input())):
        n, k = list(map(int, input().split()))
        l = list(map(int, input().split()))
        s, mx = 0, 0
        for i in range(n):
            s += l[i]
            if s < 0:
                s = 0
            mx = max(mx, s)
        ans = sum(l)
        for i in range(k):
            ans = (ans+mx) % mod
            mx = (mx*2) % mod
        print((ans) % mod)


if __name__ == "__main__":
    main()
