class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m-=1
        n-=1
        return int(factorial(m+n)/(factorial(n)*factorial(m)))