from collections import defaultdict


for i in range(int(input())):
    n = int(input())
    l = []
    for r in range(n):
        i, *j = input().split()
        l.append([i, set(j)])
    dist = [list(map(int, input().split())) for i in range(n)]
    a, b = input().split()

    d = defaultdict(list)
    for ind, (i, j) in enumerate(l):
        for v in j:
            d[v].append(ind)
    if a not in d or b not in d:
        print("""Fastest Product Not Available
Cheapest Product Not Available
""")
    else:

def main():



if __name__ == "__main__":
    main()

