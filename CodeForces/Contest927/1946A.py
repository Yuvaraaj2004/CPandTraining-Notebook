from bisect import bisect_left, bisect_right


def main():
    for i in range(int(input())):
        n = int(input())
        l = sorted((map(int, input().split())))
        if n == 1:
            print(1)
        else:
            c = 0

            for i in range(n//2-(n & 1 == 0), n):
                if l[i] == l[n//2-(n & 1 == 0)]:
                    c += 1
                else:
                    break
            print(c)


if __name__ == "__main__":
    main()
