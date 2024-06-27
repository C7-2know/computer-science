class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep=[i for i in range(len(stones))]
        size=[1 for i in range(len(stones))]
        
        def find(x):
            while rep[x]!=x:
                x=rep[x]
            return x
        
        def union(x,y):
            r_x=find(x)
            r_y=find(y)
            if size[r_x]>size[r_y]:
                rep[r_y]=r_x
                size[r_x]+=size[r_y]
            else:
                rep[r_x]=r_y
                size[r_y]+=size[r_x]
        row={}
        col={}
        for i in range(len(stones)):
            if stones[i][0] in col:
                union(col[stones[i][0]],i)
            else:
                col[stones[i][0]]=i
            
            if stones[i][1] in row:
                union(row[stones[i][1]],i)
            else:
                row[stones[i][1]]=i
            if col[stones[i][0]]!=row[stones[i][1]]:
                union(col[stones[i][0]],row[stones[i][1]])
        for i in range(len(rep)):
            rep[i]=find(rep[i])
        print(rep)
        return len(stones)-len(set(rep))
            