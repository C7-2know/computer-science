class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo={}
        nums.sort()
        count=0
        def dp(i,half_sum):
            nonlocal count
            count+=1
            if i>=len(nums):
                return half_sum==0
            if (i,half_sum) not in memo:
                memo[(i,half_sum)]=dp(i+1,half_sum-nums[i]) or dp(i+1,half_sum)
            return memo[(i,half_sum)]
        
        if sum(nums)%2!=0:
            return False
        soln=dp(1,sum(nums)//2)
        return soln