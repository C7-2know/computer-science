class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colm={}
        row={}
        three={}
        for i in range(len(board)):
            row[i]=set()
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    continue
                if j not in colm:
                    colm[j]=set()
                    colm[j].add(board[i][j])
                else:
                    if board[i][j] in colm[j]:
                        
                        return False
                    else:
                        colm[j].add(board[i][j])
                if board[i][j] in row[i]:
                    # print(row[i])
                    # print(board[i][j])
                    # print('row')
                    return False
                else:
                    row[i].add(board[i][j])
                st_r=(i//3)*3
                st_col=(j//3)*3
                end_r=st_r+3
                end_col=st_col+3
                if (end_r,end_col) in three:
                    if board[i][j] in three[(end_r,end_col)]:
                        # print('three')
                        return False
                    else:
                        three[(end_r,end_col)].add(board[i][j])
                else:
                    three[(end_r,end_col)]=set(board[i][j])
        return True
                