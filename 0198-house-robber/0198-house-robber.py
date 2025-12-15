class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def jump(i):
            if i >=len(nums):
                return 0
            if i in memo:
                return memo[i]
            take = nums[i] + jump(i+2)
            n_take = jump(i+1)
            memo[i] = n_take if n_take > take else take
            return memo[i]
        fs= jump(0)
        sc= jump(1)
        return fs if fs>sc else sc