class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir_=[(0,1),(0,-1),(1,0),(-1,0)]
        def is_valid(r,c):
            return r>=0 and r<len(matrix) and c>=0 and c<len(matrix[0])
        memo={}
        def dfs(r,c):
            nonlocal memo
            max_=1
            for rc,cc  in dir_:
                if is_valid(r+rc,c+cc) and matrix[r][c]<matrix[r+rc][c+cc]:
                    if (r+rc,c+cc) not in memo:
                        mx=dfs(r+rc,c+cc)+1
                        max_=max(mx,max_)
                    else:
                        max_=max(max_,memo[(r+rc,c+cc)]+1)
            memo[(r,c)]=max_
            return max_

        max_=0 
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                mx=dfs(r,c)
                max_=max(max_,mx)
                memo[(r,c)]=mx
        print(memo)
        return max_
