class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def dfs(r,c):

            if (r,c) not in unseen:return 0
            unseen.remove((r,c))
            return grid[r][c] + dfs(r+1,c)+dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1)
            
        m, n, ans = len(grid), len(grid[0]), 0
        unseen = {(i,j) for i,j in product(range(m),range(n))
                                                if grid[i][j]}
        while unseen: ans = max(ans,dfs(*min(unseen)))

        return ans 