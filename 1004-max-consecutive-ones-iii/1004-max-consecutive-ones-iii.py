class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_=0
        l,r=0,0
        zeros=0
        while r <len(nums):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            max_=max(max_,r-l+1)
            r+=1
        return max_