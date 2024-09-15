class Solution:
    def minCut(self, s: str) -> int:
        def isPali(st,end):
            word=s[st:end+1]
            return word==word[::-1] and len(word)>0
        memo={}
        def dp(st):
            if st>=len(s):
                return 0
            if st in memo:
                return memo[st]
            cutt=float('inf')
            for end in range(st,len(s)):
                if isPali(st,end):
                    cut=1+dp(end+1)
                    cutt=min(cutt,cut)
            memo[st]=cutt
            return memo[st]
        ans=dp(0)
        return ans-1