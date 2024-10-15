class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        for i in range(len(nums)):
            while stack and stack[-1]>nums[i] and(len(nums)-i+(len(stack)-1)>=k):
                stack.pop()
            stack.append(nums[i])
        return stack[:k]