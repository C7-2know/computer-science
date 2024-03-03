class Solution:
    def totalNQueens(self, n: int) -> int:
        res=[]
        def backtrack(st,end):
            if end==len(st):
                if valid(st):
                    cor=st.copy()
                    opt=[''.join(cor[i]) for i in range(len(cor))]
                    res.append(opt)
                return
            for i in range(len(st)):
                for j in range(end):
                    if st[j][i]=='Q':
                        break
                else:
                    st[end][i]='Q'
                    backtrack(st,end+1)
                    st[end][i]='.'
        def valid(board):
            colm=[]
            r_d=set()
            l_d=set()
            valid=True
            for i in range(len(board)):
                colm.append([])
                for j in range(len(board)):
                    colm[i].append(board[j][i])
                    if board[i][j]=='Q':
                        if i+j in l_d or i-j in r_d:
                            valid=False
                        l_d.add(i+j)
                        r_d.add(i-j)
            for i in range(len(board)):
                if board[i].count('Q')!=1:
                    valid=False
                if colm[i].count('Q')!=1:
                    valid=False
            return valid
        backtrack([['.' for _ in range(n)] for _ in range(n)],0)
        return len(res)