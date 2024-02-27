from typing import DefaultDict, List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        par=[-1 for i in range(n)]
        ns=[1 for i in range(n)]
        dist=[0 for i in range(n)]
        adj=[set() for i in range(n)]
        d=DefaultDict(dict)
        for x,y in edges:
            par[y]=x
            adj[x].add(y)
        ans=[0]*n

        def fill(node,p=-1):
            if node ==-1:return (0,0)
            dis, subn= fill(par[node], node)
            # print(node,p,(subn+ns[node]-(ns[p] if p!=-1 else 0),dis-(dist[p] if p!=-1 else 0)))
            return (dis-(dist[p] if p!=-1 else 0)+(ns[node]-(ns[p] if p!=-1 else 0)),subn+(ns[node]-(ns[p] if p!=-1 else 0)))

        def dfs(node=0):
            if len(adj[node])==0:return [0,1]
            dist[node]=len(adj[node])
            for i in adj[node]:
                x,y=dfs(i)
                dist[node]+=x
                ns[node]+=y
                d[node][i]=(x,y)
            return (dist[node],ns[node])
        ans[0]=dfs()[0]
        for i in range(1,n):
            ans[i]=fill(i)[0]
        print(ans)
        print(ns,dist)
        print(par)
        print(d)


Solution().sumOfDistancesInTree(n = 6, edges = [[0, 1],[0,2],[2,3],[2,4],[2,5]])