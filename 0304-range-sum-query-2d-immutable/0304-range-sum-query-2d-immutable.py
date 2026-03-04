class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=[[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        print(len(matrix), len(matrix[0]), len(self.matrix), len(self.matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                area=matrix[i][j]
                top_sum=0
                if i>0:
                    top_sum=self.matrix[i-1][j]
                left_sum=0
                if j>0:
                    left_sum=self.matrix[i][j-1]
                double=0
                if i>0 and j>0:
                    double=self.matrix[i-1][j-1]
                area=area+top_sum+left_sum-double
                self.matrix[i][j]=area
            print(self.matrix[i])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tot=self.matrix[row2][col2]
        left=0
        if col1>0:
            left=self.matrix[row2][col1-1]
        top=0
        if row1-1>=0:
            top=self.matrix[row1-1][col2]
        double=0
        if row1>0 and col1>0:
            double=self.matrix[row1-1][col1-1]
        return tot-left-top+double
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)