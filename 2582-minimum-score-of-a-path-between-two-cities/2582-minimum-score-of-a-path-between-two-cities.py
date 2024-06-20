class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent=[(i,float("inf")) for i in range(n)]

        def find(x):
            while parent[x][0]!=x:
                parent[x]=parent[parent[x][0]]
                x=parent[parent[x][0]][0]
            return x

        def union(x,y,dist):
            px=find(x-1)
            py=find(y-1)
            min_dis=min(parent[px][1],dist)
            if parent[py][1]>min_dis:
                parent[py]=(py,min_dis)
            parent[px]=parent[py]
            

        for con in roads:
            union(con[0],con[1],con[2])
        min_=find(parent[0][0])
        return parent[min_][1]
