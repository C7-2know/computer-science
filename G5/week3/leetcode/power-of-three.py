class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(n)
        if n==1.0:
            return True
        if n<1:
            print(n)
            return False
        return self.isPowerOfThree(n/3)