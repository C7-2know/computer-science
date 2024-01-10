class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique={}
        max_sum=0
        summ=0
        left=0
        for i in range(len(nums)):
            if nums[i] in unique:
                while left<=unique[nums[i]]:
                    summ-=nums[left]
                    left+=1
            unique[nums[i]]=i
            summ+=nums[i]
            max_sum=max(summ,max_sum)
        return max_sum