class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_=max(nums)
        return nums.index(max_)