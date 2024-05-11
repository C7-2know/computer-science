class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def rec(n):
            if n<2:
                return n
            if n==2:
                return 1
            if n not in memo:
                memo[n]=rec(n-1)+rec(n-2)+rec(n-3)
            return memo[n]
        return rec(n)