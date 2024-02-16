class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_=0
        ins_p=0
        for i in s:
            if i=='(':
                open_+=1
            elif i==')':
                if open_>0:
                    open_-=1
                else:
                    ins_p+=1
            # else:
            #     return
        return open_+ins_p