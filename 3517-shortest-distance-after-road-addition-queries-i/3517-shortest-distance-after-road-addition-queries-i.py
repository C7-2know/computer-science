class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dc={i:[i+1] for i in range(n)}
        def find_dis():
            d=0
            visited=set()
            queue=[0]
            while queue:
                new=[]
                for cur in queue:
                    visited.add(cur)
                    for nbr in dc[cur]:
                        if nbr==n-1:
                            return d+1
                        if nbr not in visited:
                            new.append(nbr)
                d+=1
                queue=new
            return d
        ans=[]
        for q in queries:
            dc[q[0]].append(q[1])
            ans.append(find_dis())
        return ans

