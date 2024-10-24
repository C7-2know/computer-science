class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_=max(nums)
        ans=0
        for i in range(k):
            ans+=max_
            max_+=1
        return ans