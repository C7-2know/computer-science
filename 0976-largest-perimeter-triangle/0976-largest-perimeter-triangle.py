class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i=len(nums)-3
        max_=0
        while i>=0:
            if nums[i]+nums[i+1]>nums[i+2]:
                max_=max(max_, nums[i]+nums[i+1] + nums[i+2])
            i-=1
        return max_