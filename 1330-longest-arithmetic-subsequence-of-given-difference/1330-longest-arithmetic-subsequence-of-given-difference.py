class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo={}
        # def dp(st,end):
        #     if st>=len(arr) or end>=len(arr):
        #         return 0
        #     if (st,end) not in memo:
        #         if arr[end]-arr[st]==difference:
        #             memo[(st,end)] =1 + max(dp(st+1,end+1),dp(st,end+1))
        #         else:
        #             memo[(st,end)]= max(dp(st+1,end),dp(st,end+1))
        #     print(memo)
        #     return memo[(st,end)]
        # return dp(0,0)

        #Bottom up approach
        # dp=[1 for _ in range(len(arr))]
        # for i in range(len(arr)):
        #     found=False
        #     for j in range(i+1,len(arr)):
        #         if arr[j]-arr[i]==difference and dp[i]>=dp[j]:
        #             dp[j]=dp[i]+1
        #             found=True
        #             bf=j
        #         if found:
        #             break
        memo={}
        max_=0
        for i in arr:
            if i-difference in memo:
                memo[i]=memo[i-difference]+1
            else:
                memo[i]=1
            max_=max(max_,memo[i])
        return max_
    
               
        return max(dp)


                    