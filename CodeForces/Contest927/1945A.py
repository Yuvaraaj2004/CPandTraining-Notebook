from math import ceil


def main():
    for i in range(int(input())):
        a, b, c = list(map(int, input().split()))
        if b % 3 != 0:
            mod = b % 3
            b += 3-mod
            c -= 3-mod
        # print(a, b, c)
        print(a+ceil((b+c)/3) if c >= 0 else -1)


if __name__ == "__main__":
    main()
