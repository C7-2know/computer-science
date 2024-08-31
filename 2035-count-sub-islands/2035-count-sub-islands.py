class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        islands=[]
        visited=set()
        def isvalid(r,c):
            return r>=0 and r<len(grid2) and c<len(grid2[0]) and c>=0
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(r,c,island):
            nonlocal visited
            if r>len(grid2) or c>len(grid2[0]) or r<0 or c<0:
                return island
            visited.add((r,c))
            for rr,cc in direction:
                if isvalid(r+rr,c+cc) and grid2[r+rr][c+cc]==1 and (r+rr,c+cc) not in visited:
                    island.append((r+rr,c+cc))
                    island=dfs(r+rr,c+cc,island)
            return island
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if (r,c) not in visited and grid2[r][c]==1:
                    island=dfs(r,c,[(r,c)])
                    if len(island)>0:
                        islands.append(island)
        def is_sub(set_):
            for r,c in set_:
                if grid1[r][c]!=1:
                    return False
            return True
        count=0
        for val in islands:
            if is_sub(val):
                count+=1
        return count
