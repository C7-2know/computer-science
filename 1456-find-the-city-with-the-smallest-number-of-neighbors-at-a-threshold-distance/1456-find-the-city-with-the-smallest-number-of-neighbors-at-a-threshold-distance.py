class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=[[] for _ in range(n)]
        for edge in edges:
            if edge[2]<=distanceThreshold:
                
                adj[edge[0]].append((edge[2],edge[1]))
                adj[edge[1]].append((edge[2],edge[0]))
        def explore(i,t):
            nbrs=adj[i].copy()
            visited=set([i])
            heapify(nbrs)
            while nbrs:
                w,cur=heappop(nbrs)
                if w>t:
                    continue
                visited.add(cur)
                for nw,nbr in adj[cur]:
                    if w+nw<=t and nbr not in visited:
                        heappush(nbrs,(nw+w,nbr))
                    
            return len(visited)-1
        node=0
        min_=float('inf')
        for i in range(len(adj)):
            ex=explore(i,distanceThreshold)
            if ex<=min_:
                min_=ex
                node=i
        
        return node

