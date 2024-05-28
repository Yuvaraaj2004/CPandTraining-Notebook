def main():
    for i in range(int(input())):
        n = int(input())
        print(13*(n//2)+(6 if n & 1 else 0))


if __name__ == "__main__":
    main()
