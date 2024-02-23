class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gp=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=gp-i:
                gp=i
        if nums[i]<gp-i:
            return False
        return True
