class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_=bin(n)
        count=0
        for i in bin_[2:]:
            if i=='1':
                count+=1
        return count