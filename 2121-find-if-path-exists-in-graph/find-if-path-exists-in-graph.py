class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=[[] for _ in range(n)]
        for edge in edges:
            n1,n2=edge
            graph[n1].append(n2)
            graph[n2].append(n1)
        stack=[source]
        visited=set()
        def dfs(s,d):
            if s==d:
                return True
            visited.add(s)
            for nbr in graph[s]:
                if nbr not in visited:
                    visited.add(nbr)
                    found = dfs(nbr,d)
                    if found:
                        return found
            return False
        return dfs(source, destination)
          