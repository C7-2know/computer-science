class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return 0
        nums.sort()
        n=len(nums)-1
        min_=float('inf')
        for i in range(4):
            mx=nums[n-(3-i)]
            mn=nums[i]
            min_=min(min_,mx-mn)
        return min_
