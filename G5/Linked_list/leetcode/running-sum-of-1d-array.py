class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # sm_=0
        # for i in range(len(nums)):
        #     sm_+=nums[i]
        #     nums[i]=sm_
        # return nums

        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums