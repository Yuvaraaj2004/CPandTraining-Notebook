from icecream import ic


def f(n, i):
    if n == 0:
        return ''
    return f(n//i, i)+str(n % i)


l, s = [], set()
for i in range(2, 36):
    x, v = f'{i-1}{i-1}', 1
    l.append([])
    while v < 10**6:
        x += f"{i-1}"
        v = int(x, i)-v
        l[-1].append(v)
        s.add(i)
ic(l)


def main():
    for i in range(int(input())):
        n = int(input())

        # print(n, [(i, f(n, i)) for i in range(2, n)])


if __name__ == "__main__":
    main()
