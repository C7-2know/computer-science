class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.row_sum=[]
        for i in range(len(self.matrix)):
            self.row_sum.append(sum(self.matrix[i]))
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result=0
        for i in range(row2-row1+1):
            result+=self.row_sum[row1+i]-sum(self.matrix[row1+i][:col1])-sum(self.matrix[row1+i][col2+1:])
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)