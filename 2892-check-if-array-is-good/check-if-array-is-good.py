class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        return len(nums)==len(set(nums))+1 and nums[-1]==nums[-2]==len(nums)-1