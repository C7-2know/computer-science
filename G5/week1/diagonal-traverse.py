class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_d={k:[] for k in range(len(mat)+len(mat[0])-1)}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                num_d[i+j].append(mat[i][j])
        arr=[]
        for i in num_d:
            if i%2==0:
                num_d[i]=num_d[i][::-1]
            arr.extend(num_d[i])
        return arr
