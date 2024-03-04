class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        while n>3:
            if n %4!=0:
                return False
            n=n/4
        return n==1
