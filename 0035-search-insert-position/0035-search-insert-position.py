class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        mid=(left+right)//2
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]==target:
                return mid
            else:
                right=mid
        return right