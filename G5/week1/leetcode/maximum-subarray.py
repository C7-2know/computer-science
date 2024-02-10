class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ind=0
        min_=min(0,nums[0])
        max_=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            max_=max(max_,nums[i]-min_)

            if nums[i]<min_:
                min_=nums[i]
            # print(nums)
            # print(min_,nums)
        return max_