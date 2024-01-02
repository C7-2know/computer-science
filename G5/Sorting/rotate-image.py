class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            for j in range(i,len(matrix)-1-i):
                r=i
                dis=len(matrix)-1-2*i
                print('turn',r,j,'dis',dis)
                c=dis+j
                if c>dis+i:
                    rem=c-(dis+i)
                    c=dis+i
                    r+=rem
                print(r,c)
                
                matrix[r][c],matrix[i][j] =matrix[i][j],matrix[r][c]
                r+=dis
                if r>dis+i:
                    rem=r-(dis+i)
                    c-=rem
                    r=dis+i
                print(r,c)
                matrix[r][c],matrix[i][j] =matrix[i][j],matrix[r][c]
                c-=dis
                if c<i:
                    rem=i-c
                    r-=rem
                    c=i
                print(r,c)
                matrix[r][c],matrix[i][j]=matrix[i][j],matrix[r][c]
                print('finally',matrix[i])

