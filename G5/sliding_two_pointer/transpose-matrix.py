class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_mat=[[] for k in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_mat[j].append(matrix[i][j])
        return new_mat
            
    