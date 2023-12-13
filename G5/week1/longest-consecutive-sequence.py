class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        max_lent=1
        lent=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]-1:
                lent+=1
                max_lent=max(lent,max_lent)
            elif nums[i]==nums[i+1]:
                pass
            else:
                lent=1
        return max_lent
