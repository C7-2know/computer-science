class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        summ=0
        i=0 
        while i+3<=len(grid[0]):
            j=0
            while j+3<=len(grid):
                sum1=sum(grid[j][i:i+3])+grid[j+1][i+1]+sum(grid[j+2][i:i+3])
                # sum1=0
                print(sum(grid[j][i:i+3]))
                j+=1
                summ=max(summ,sum1)
            i+=1
                
        return summ
        