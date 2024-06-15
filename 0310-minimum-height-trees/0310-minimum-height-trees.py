class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph=[[] for _ in range(n)]
        size=[0 for _ in range(n)]
        for i in edges:
            size[i[0]]+=1
            size[i[1]]+=1
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        queue=deque()
        height=0
        for nei in range(len(graph)):
            if len(graph[nei])==1:
                queue.append(nei)
        while queue:
            if n<=2:
                return queue
            for i in range(len(queue)):
                node=queue.popleft()
                n-=1
                for nei in graph[node]:
                    size[nei]-=1
                    if size[nei]==1:
                        queue.append(nei)
       