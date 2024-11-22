class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dc={}
        for i in range(len(matrix)):
            pat="0"
            st=0
            for j in range(1,len(matrix[0])):
                if matrix[i][j-1]!=matrix[i][j]:
                    st=abs(st-1)
                pat+=str(st)
            dc[pat]=dc.get(pat,0)+1
        return max(dc.values())