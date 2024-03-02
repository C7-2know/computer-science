class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(open_,close,par):
            if open_==0 and close==0:
                pair=''.join(par)
                if pair not in ans:
                    ans.append(pair)
                return 
            if open_>0:
                par.append('(')
                backtrack(open_-1,close,par)
                par.pop()
            if close>open_:
                par.append(')')
                backtrack(open_,close-1,par)
                par.pop() 
            return
        backtrack(n,n,[]) 
        return ans
            


        # res=[]
        # def backtrack(open_,close,para):
        #     if open_==0 and close==0:
        #         res.append(''.join(para))
        #         return                    
        #     if open_>0:
        #         para+=['(']
        #         backtrack(open_ - 1,close,para)
        #         para.pop()

        #     if close>open_:
        #         para += [")"]
        #         backtrack(open_ ,close - 1,para)
        #         para.pop()
           
        # backtrack(n,n,[])
        # return res
                

            
