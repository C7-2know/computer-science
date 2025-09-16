class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def is_non_p(n):
            for i in str(n):
                if i == "0":
                    return False
            return True
        i=1
        while i<n:
            if is_non_p(i) and is_non_p(n-i):
                return [i,n-i]
            i+=1