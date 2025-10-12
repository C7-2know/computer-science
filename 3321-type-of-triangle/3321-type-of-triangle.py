class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if (nums[0]+nums[1]) <= nums[2]:
            return "none"
        set_=set(nums)
        if len(set_)== len(nums):
            return "scalene"
        elif len(set_)==2:
            return "isosceles"
        else:
            return "equilateral"