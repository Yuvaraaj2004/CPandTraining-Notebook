from collections import Counter


def main():
    for i in range(int(input())):
        s = input()
        d = Counter(s)
        ans = float('inf')
        for i in d:
            c, l = 0, 0
            for ind, j in enumerate(s):
                if j == i:
                    c += 1
                if ind >= d[i]-1:
                    ans = min(ans, d[i]-c)
                    # print(i, s[l:ind+1], d[i]-c)
                    c -= (s[l] == i)
                    l += 1
        print(ans)


if __name__ == "__main__":
    main()
