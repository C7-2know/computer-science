class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # i=0
        # while i <len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         i+=3
        #     else:
        #         return nums[i]
        
        # return nums[i]

        once,twice=0,0
        for i in nums:
            once=(once^i)&(~twice)
            twice=(twice^i)&(~once)
        return once