class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ones=set()
        cols={}
        rows={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    cols[j] = cols.get(j,0)+1
                    rows[i] = rows.get(i,0)+1
                    ones.add((i,j))
        count = 0
        for r,c in ones:
            if cols[c]==1 and rows[r]==1:
                count+=1
        return count
