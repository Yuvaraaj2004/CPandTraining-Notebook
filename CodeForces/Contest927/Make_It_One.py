from collections import defaultdict


def main():
    for i in range(int(input())):
        a, b = list(map(int, input().split()))
        # d = defaultdict(set)
        # for i in range(a, b+1):
        #     j, v = 2, i
        #     while j*j <= i:
        #         if i % j == 0:
        #             d[j].add(v)
        #         while i % j == 0:
        #             i //= j
        #         j += 1
        #     if v == 1 or i != 1:
        #         d[i].add(v)
        # l = []
        # for i in d:
        #     for j in d[i]:
        #         for k in d:
        #             if j not in d[k]:
        #                 l += [i, j]

        if (b-a+1) & 1:
            print(b, end=' ')
        for i in range(a, (b)+(-1 if (b-a) & 1 else 0), 2):
            print(i+1, i, end=' ')
        print()


if __name__ == "__main__":
    main()
