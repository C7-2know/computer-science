class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
        nbrs=[[] for _ in range(n)]
        for n1, n2 in edges:
            nbrs[n1].append(n2)
            nbrs[n2].append(n1)
        
        edge_cnt=[len(nbr) for nbr in nbrs]
        leaves=[]
        for i in range(n):
            if edge_cnt[i]==1:
                leaves.append(i)
        
        stack=leaves
        while stack:
            next_=[]
            for node in stack:
                for nbr in nbrs[node]:
                    edge_cnt[node]-=1
                    edge_cnt[nbr]-=1
                    if edge_cnt[nbr]==1:
                        next_.append(nbr)
            if len(next_)==0:
                return stack
            stack=next_

