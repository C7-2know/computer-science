class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_=0
        l,r=0,0
        sum_=0
        while r <len(nums):
            sum_+=nums[r]
            while sum_>0 and sum_+k<(r-l+1):
                sum_-=nums[l]
                l+=1
            max_=max(max_,min(sum_+k, len(nums)))
            r+=1
        return max_