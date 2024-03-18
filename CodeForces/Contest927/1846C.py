
def main():
    for i in range(int(input())):
        a, b, c = list(map(int, input().split()))
        l = [sorted(map(int, input().split())) for i in range(a)]
        ans = []
        for ind, i in enumerate(l):
            s, p, j = 0, 0, 0
            while j < len(i) and s+i[j] <= c:
                s += i[j]
                p += s
                j += 1
            ans.append((-j, p, ind))
        ans.sort()
        # print(ans)
        for ind, i in enumerate(ans):
            if i[2] == 0:
                print(ind+1)
                break


if __name__ == "__main__":
    main()
