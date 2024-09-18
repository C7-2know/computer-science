class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=max(nums)
        m=0
        count=0
        for i in nums:
            if i==mx:
                count+=1
            else:
                m=max(m,count)
                count=0
        m=max(m,count)
        print(m)
        return m