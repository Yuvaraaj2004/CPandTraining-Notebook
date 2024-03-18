from collections import Counter, defaultdict


def main():
    for i in range(int(input())):
        l, f = [input() for i in range(3)], 0
        for i in range(3):
            d = defaultdict(int)
            for j in range(3):
                d[l[i][j]] += 1
            # print(d)
            if len(d) == 1:
                if (v := list(d.items())[0][0]) != '.':
                    print(v)
                    f = True
                    break
        if not f:
            for i in range(3):
                d = defaultdict(int)
                for j in range(3):
                    d[l[j][i]] += 1
                # print(d)
                if len(d) == 1:
                    if (v := list(d.items())[0][0]) != '.':
                        print(v)
                        f = True
                        break
        if not f:
            d = Counter(l[i][i] for i in range((3)))
            if len(d) == 1:
                if (v := list(d.items())[0][0]) != '.':
                    print(v)
                    f = True

        if not f:
            d = Counter(l[i][-i-1] for i in range((3)))
            if len(d) == 1:
                if (v := list(d.items())[0][0]) != '.':
                    print(v)
                    f = True
        if not f:
            print('DRAW')


if __name__ == "__main__":
    main()
