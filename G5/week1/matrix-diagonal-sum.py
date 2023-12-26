class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i-j==0 or i+j==len(mat)-1:
                    summ+=mat[i][j]
        # if len(mat)%2!=0:
        #     ind=len(mat)//2 
        #     summ-=mat[ind][ind]
        return summ

        