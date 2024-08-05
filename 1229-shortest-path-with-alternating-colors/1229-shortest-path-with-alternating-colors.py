class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=[[[],[]] for _ in range(n)]
        # 0--- red, 1---blue
        for a,b in redEdges:
            graph[a][0].append(b) 
        for a,b in blueEdges:
            graph[a][1].append(b) 
        queue=[(0,0),(0,1)]
        visited=set([(0,0),(0,1)])
        out=[0]+[-1 for _ in range(n-1)]
        dist=0
        while queue:
            new=[]
            while queue:
                node,color=queue.pop()
                alt=1-color
                for n in graph[node][alt]:
                    if (n,alt) not in visited:
                        new.append((n,alt))
                        visited.add((n,alt))
                    if out[n]==-1:
                        out[n]=dist+1
            dist+=1
            queue=new
        return out