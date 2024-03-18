
from bisect import bisect_right


def Solve():
    n, m, c = list(map(int, input().split()))
    a, b = sorted(map(int, input().split())), sorted(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > c:
            break
        else:
            ans += bisect_right(b, c-a[i])

    print(ans)


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
