import heapq


for t in range(int(input())):
    n, score = int(input()), list(map(int, input().split()))
    edges = [set() for i in range(n)]
    for i in range(n-1):
        x, y = list(map(int, input().split()))
        x -= 1
        y -= 1
        edges[x].add(y)
        edges[y].add(x)
    # print(edges)
    l, q = [], set()
    for ind, i in enumerate(score):
        if len(edges[ind]) & 1:
            l.append((-i, len(edges[ind]), ind))
            q.add(ind)
    heapq.heapify(l)
    # print(l)
    ans, visited = [], set()
    while l:
        s, leng, ind = heapq.heappop(l)
        if ind not in q and ind not in visited:
            continue
        for i in edges[ind]:
            edges[i] -= {ind}
            if i not in q and i not in visited and len(edges[i]) & 1:
                heapq.heappush(l, (-score[i], len(edges[i]), i))
                q.add(i)
            else:
                q -= {i}
        # print(l, q, visited)
        visited.add(ind)
        ans += [ind+1]
    print([i+1 for i in visited])
