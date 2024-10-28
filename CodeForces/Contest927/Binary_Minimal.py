cp


def Solve():
    a, b = GetL()
    s = list(GetS())

    rem = set()
    for ind, i in enumerate(s):
        if i == '1' and b:
            rem.add(ind)
            b -= 1
    s = [i for ind, i in enumerate(s) if ind not in rem]
    while b:
        s.pop()
        b -= 1
    print(''.join(s))


if __name__ == "__main__":
    for i in range(int(input())):
        Solve()
