edges = int(input())
n = int(input())
adjM = [[0]*n for i in range(n)]
adj = [[] for i in range(n)]
for i in range(edges):
    x, y, z = map(int, input().split())
    adj[x].append((y, z))
    adjM[x][y] = z
for i in adjM:
    print(i)
print()
ans = 0
while True:
    visited = [False]*n
    par = [-1]*n
    q = [0]
    while q:
        node = q.pop()
        for ind, i in enumerate(adjM[node]):
            if not visited[ind] and i > 0:
                par[ind] = node
                visited[ind] = True
                q.append(ind)
    if visited[-1] != True:
        break
    cur, val = n-1, float('inf')
    v = []
    while cur != 0:
        v.append(cur)
        val = min(val, adjM[par[cur]][cur])
        cur = par[cur]
    v.append(cur)
    print(v, val)
    cur = n-1
    while cur != 0:
        adjM[cur][par[cur]] += val
        adjM[par[cur]][cur] -= val
        cur = par[cur]

    for i in adjM:
        print(i)
    print()
    ans += val

print(ans)
