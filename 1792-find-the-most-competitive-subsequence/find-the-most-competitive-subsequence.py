class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack=[nums[0]]
        for i in range(1,len(nums)):
            while stack and stack[-1]>nums[i] and len(stack)+(len(nums)-1-i)>=k:
                stack.pop()
            if not stack or len(stack)<k:
                stack.append(nums[i])
        return stack