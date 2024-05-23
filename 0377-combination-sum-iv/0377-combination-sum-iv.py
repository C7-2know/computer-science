class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # memo={}
        # def dp(i,num):
        #     if num==0:
        #         return 1
        #     if i>=len(nums) or num<0:
        #         return 0
        #     ans=0
        #     for j in range(i,len(nums)):
        #         ans+=dp(j+1,num)+dp(j,num-nums[i])
        #     # if i==2 and num==0:
        #     #     print(True)
        #     print(memo)
        #     memo[i]=ans
        #     return ans
        # return dp(0,4)

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

        # dp=[[0 for _ in range(target+1)] for j in range(len(nums))]
        # dp[0][0]=1

        # for i in range(len(nums)):
        #     # if nums[i]<j:
        #     #         continue
        #     for j in range(target+1):
                
        #         if j-nums[i]>=0 and i-1>=0:
        #             dp[i][j]=dp[i-1][j]+dp[i][j-nums[i]]
        #         else:
        #             dp[i][j]=dp[i][j-1]
        # print(dp)
        # return dp[len(nums)-1][target]
                    
