class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dc={1:'', 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'],
             7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        ans=[]
        def letterComb(digit,st,ind):
            if len(st)==len(digit):
                if st==[]:
                    return
                ans.append(''.join(st))
                return
            key=int(digit[ind])
            for i in range(len(dc[key])):
                st+=dc[key][i] 
                letterComb(digit,st,ind+1)
                st.pop()           
            return
        letterComb(digits,[],0)
        return ans
            