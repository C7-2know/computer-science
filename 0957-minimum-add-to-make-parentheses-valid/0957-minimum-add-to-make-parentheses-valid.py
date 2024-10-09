class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op=0
        close=0
        for i in s:
            if i=="(":
                op+=1
            else:
                if op>0:
                    op-=1
                else:
                    close+=1
        return op+close