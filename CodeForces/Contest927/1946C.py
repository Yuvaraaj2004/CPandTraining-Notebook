from sortedcontainers import SortedDict


def main():
    for i in range(int(input())):
        n, k = list(map(int, input().split()))
        edges = [[] for i in range(n+1)]
        for i in range(n):
            x, y = list(map(int, input().split()))
            edges[x].append(y)

        def dfs(node=1):
            sz = 1
            for i in edges[node]:
                sz += dfs(i)

            if sz > mx:
                sz, c[0] = 0, c[0]+1

        l, r, ans = 1, n, 0
        while l < r:
            mx, c = (l+r)//2, [0]
            dfs()
            if c[0] <= k:
                ans = l
                l = mx+1
            else:
                r = mx-1
        print(l)


if __name__ == "__main__":
    main()

SortedDict()
