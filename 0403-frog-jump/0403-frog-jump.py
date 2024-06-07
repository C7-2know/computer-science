class Solution:
    def canCross(self, stones: List[int]) -> bool:
        count=0 
        memo={}
        def dp(i,u,st):
            if i>=len(stones):
                return False
            if i==len(stones)-1 and st+u!=stones[i]:
                return False
            if i==len(stones)-1 and st+u==stones[i]:
                return True
            if st+u<stones[i]:
                return False
            if st+u>stones[i]:
                memo[(i,u,st)]=dp(i+1,u,st)
            if (i,u,st) not in memo:
                memo[(i,u,st)]=dp(i+1,u,stones[i])or dp(i+1,u+1,stones[i])or dp(i+1,u-1,stones[i])
            return memo[(i,u,st)]
        return dp(0,1,0)