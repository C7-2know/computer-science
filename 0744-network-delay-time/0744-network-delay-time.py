class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={}
        for move in times:
            if move[0] not in graph:
                graph[move[0]]=[]
            graph[move[0]].append(move[1:])
        min_=0
        heap=[(0,k)]
        heapify(heap)
        visited=set()
        while heap:
            t,cur=heappop(heap)
            if cur in visited:
                continue
            visited.add(cur)
            min_=max(t,min_)
            if cur not in graph:
                continue
            for nbr,nt in graph[cur]:
                if nbr not in visited:
                    heappush(heap,(t+nt,nbr))

        return min_ if len(visited)==n else -1
