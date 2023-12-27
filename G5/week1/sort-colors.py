class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for k in range(i,0,-1):
                if i==3:
                    print(k)
                    print(nums)

                if nums[k]<nums[k-1]:
                    nums[k],nums[k-1]=nums[k-1],nums[k]