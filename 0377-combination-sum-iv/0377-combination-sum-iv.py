class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={}
        def dp(i,num):
            if i>=len(nums) or num>target:
                return 0
            if num==target:
                return 1
            if (i,num )in memo:
                return memo[(i,num )]
            ans=0
            for n in range(len(nums)):
                ans+=dp(n,num+nums[n])
            memo[(i,num )]=ans
            return memo[(i,num )]
        return dp(0,0)

        