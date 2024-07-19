class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        isBip=True
        visited=set()
        def dfs(node):
            nonlocal isBip,visited
            cl=1
            if color[node]==1:
                cl=0 
            for nbr in graph[node]:
                if color[nbr]!=-1 and color[nbr]!=cl:
                    return False
                color[nbr]=cl
                if nbr not in visited:
                    visited.add(nbr)
                    isBip=dfs(nbr)
                    if not isBip:
                        return False    
            return True

        for i in range(len(graph)):
            if i not in visited:
                if color[i]==-1:
                    color[i]=0
                visited.add(i)
                isBip=dfs(i)
                if not isBip:
                    return False            
        return isBip
        
        