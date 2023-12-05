class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_max=0
        max_one=0
        for i in range(len(nums)):
            if nums[i]==1:
                max_one+=1
            else:
                prev_max=max(prev_max, max_one)
                max_one=0
        return max(prev_max,max_one)