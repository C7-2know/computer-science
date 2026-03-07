class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def robb(ind):
            nonlocal memo
            if ind>=len(nums):
                return 0
            if ind not in memo:
                memo[ind] = max(nums[ind]+robb(ind+2), robb(ind+1))
            return memo[ind]
        return robb(0)