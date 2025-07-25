class Solution:
    def maxSum(self, nums: List[int]) -> int:
        set_=set(nums)
        nums=list(set_)
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]<0:
                i+=1
            else:
                break
        return sum(nums[i:])