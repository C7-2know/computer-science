class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        last={}
        i=0
        sum_=0
        max_=0
        rep=-1
        while i <len(nums):
            sum_+=nums[i]
            if i>=k:
                sum_-=nums[i-k]
            if nums[i] in last and last[nums[i]]+k>i:
                rep=max(rep,last[nums[i]])
            elif i-rep>=k:                
                max_=max(sum_,max_)
            last[nums[i]]=i
            i+=1
        return max_
