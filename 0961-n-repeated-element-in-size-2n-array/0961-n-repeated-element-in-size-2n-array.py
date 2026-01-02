class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        return (sum(nums)-sum(list(set(nums))))//(n-1)