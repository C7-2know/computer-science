class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev={}
        for i in range(len(nums)):
            sec=target-nums[i]
            if sec in prev:
                return [i, prev[sec]]
            prev[nums[i]]=i
