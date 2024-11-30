class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n+1]*(n+1)
        dp[0]=0
        def find(target):
            nonlocal dp
            if dp[target] != (n+1):
                return dp[target]
            for s in range(1,target+1):
                square=s*s
                if target-square<0:
                    break
                dp[target] = min(dp[target], find(target-square)+1)
            return dp[target]

        return find(n)
