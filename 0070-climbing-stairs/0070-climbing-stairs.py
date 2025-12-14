class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def climb(cur):
            if cur==n:
                return 1
            if cur in memo:
                return memo[cur]
            if cur>n:
                return 0
            memo[cur] = climb(cur+1) + climb(cur+2)
            return memo[cur]
        return climb(0)