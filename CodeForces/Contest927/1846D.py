def main():
    for i in range(int(input())):
        a, b, c = list(map(int, input().split()))
        b /= 2
        l = [float('inf')]+sorted(map(int,
                                      input().split()), reverse=True)
        ans, base, m = 0, b*c, c/(b)
        print(base, m, l)

        for j in range(1, len(l)):
            diff = l[j-1] - l[j]
            # print((max(0, diff), ((b)-diff*m)))
            ans += base-(diff * ((b)-diff*m) if diff <= c else 0)
        print(ans)
        print()


if __name__ == "__main__":
    main()
