class Solution:
    def integerBreak(self, n: int) -> int:
        memo={0:0,1:1,2:1}
        def dp(num):
            if num<=0:
                return 0
            if num<=2:
                return 1     
            if num not in memo:
                max_=0
                for i in range(1,num):
                    max_=max(max_,dp(num-i)*i,i*(num-i))
                memo[num]=max_
            return memo[num]
        return dp(n)
