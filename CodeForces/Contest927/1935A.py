def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        if s <= s[::-1]:
            print(s if not (n & 1) else s+s[::-1])
        else:
            print(s[::-1] if (n & 1) else s[::-1]+s)
            # print()


if __name__ == "__main__":
    main()
