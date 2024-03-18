

def main():
    for i in range(int(input())):
        a, b = list(map(int, input().split()))
        c = 0
        while a != 1:
            # print(a)
            c += a//2
            a = (a >> 1)+(a != 1 and a & 1)
        print('YES' if c >= b else 'NO')


if __name__ == "__main__":
    main()
