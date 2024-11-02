class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dir_=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    queue.append((i,j))
                    
        def is_valid(r,c):
            return r>=0 and r<len(grid) and c>=0 and c<len(grid[0])
        count=0
        visited=set()
        while queue:
            new=[]
            for r,c in queue:
                for rc,cc in dir_:
                    if is_valid(rc+r,c+cc) and (r+rc,c+cc) not in visited and grid[r+rc][c+cc]!=1:
                        visited.add((r+rc,c+cc))
                        new.append((r+rc,c+cc))
            queue=new
            if new:
                count+=1

        return count if count>0 else -1
                
