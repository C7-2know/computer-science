class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[i for i in nums]
        arr.sort()
        for i in range(len(nums)):
            nums[i]=arr.index(nums[i])
        return nums
