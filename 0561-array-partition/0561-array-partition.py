class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        sum_=0
        while i<len(nums):
            sum_+=nums[i]
            i+=2
        return sum_