class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_= float('inf')
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if i+k-1>=len(nums):
                break
            min_= min(min_, nums[i]-nums[i+k-1])
        return min_ if min_ else 0