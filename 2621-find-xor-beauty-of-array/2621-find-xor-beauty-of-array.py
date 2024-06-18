class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res^=i
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(len(nums)):
        #             res^=((nums[i] | nums[j])& nums[k])
        return res
