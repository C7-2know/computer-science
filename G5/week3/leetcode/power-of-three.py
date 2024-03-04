class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1.0:
            return True
        if n<1:
            return False
        return self.isPowerOfThree(n/3)