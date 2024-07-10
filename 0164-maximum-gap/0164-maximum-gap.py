class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_=float('-inf')
        if len(nums)<2:
            return 0
        for i in range(1,len(nums)):
            max_=max(max_,nums[i]-nums[i-1])
        return max_