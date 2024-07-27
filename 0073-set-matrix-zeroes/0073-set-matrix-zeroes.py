class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col=set(),set()
        def is_valid(r,c):
            return r>=0 and r<len(matrix) and c>=0 and c<len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
                    for r in range(i):
                        matrix[r][j]=0
                    
                    for c in range(j):
                        matrix[i][c]=0
                else:
                    if i in row or j in col:
                        matrix[i][j]=0
                    
        
        
        