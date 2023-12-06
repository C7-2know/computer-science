class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i]<(nums[i+2]+nums[i+1]):
                return sum(nums[i:i+3])
        return 0 
