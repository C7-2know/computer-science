class Solution:
    def monkeyMove(self, n: int) -> int:
        memo={}
        def half(n):
            if n==1:
                return 2
            if n not in memo:
                memo[n]=(half(n//2)*half(n-n//2))%(10**9+7)
            return memo[n]
        hal=half(n//2)
        h=half(n-n//2)
        res=(hal*h)
        res-=2
        return res%(10**9+7)
