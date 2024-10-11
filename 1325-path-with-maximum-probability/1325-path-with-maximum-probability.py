class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        processed=set()
        graph=[[] for _ in range(n+1)]
        for i in range(len(edges)):
            u,v=edges[i]
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        prob=[0 for _ in range(n+1)]
        heap=[]
        heapify(heap)

        for nbr,p in graph[start_node]:
            heappush(heap,(-p,nbr))
        while heap:
            p,cur=heappop(heap)
            processed.add(cur)
            prob[cur]=max(prob[cur],-p)
            for nbr,pr in graph[cur]:
                if nbr not in processed:
                    heappush(heap,(-(-p*pr),nbr))
        return prob[end_node]


        