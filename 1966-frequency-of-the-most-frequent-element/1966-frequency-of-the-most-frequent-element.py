class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=ans=tot=0
        for j in range(len(nums)):
            tot+=nums[j]
            while nums[j] * (j-i+1) > tot + k :
                tot -= nums[i]
                i+=1
            ans = max(ans,j-i+1)
        return ans