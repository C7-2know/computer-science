class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     for k in range(i,0,-1):
        #         if i==3:
        #             print(k)
        #             print(nums)
        #         if nums[k]<nums[k-1]:
        #             nums[k],nums[k-1]=nums[k-1],nums[k]

        left=0
        while left<len(nums):
            right=len(nums)-1
            while right>left:
                if nums[left]>nums[right]:
                    nums[left],nums[right]=nums[right],nums[left]
                right-=1
            left+=1
        
        