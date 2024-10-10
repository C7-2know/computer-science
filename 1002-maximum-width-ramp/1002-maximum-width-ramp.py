class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack=[0]
        for i in range(1,len(nums)):
            if nums[stack[-1]]>nums[i]:
                stack.append(i)
        max_=0
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                ind=stack.pop()
                max_=max(max_,i-ind)
            
        return max_