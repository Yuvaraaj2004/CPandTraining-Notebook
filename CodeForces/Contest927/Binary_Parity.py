def main():
    for i in range(int(input())):
        n = int(input())
        c = 0
        while n:
            c, n = c+n & 1, n >> 1
        print('EVEN' if c & 1 == 0 else 'ODD')


if __name__ == "__main__":
    main()
