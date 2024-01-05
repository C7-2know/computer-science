class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum=sum(nums[:k])
        max_sum=w_sum
        for i in range(1,len(nums)-(k-1)):
            w_sum=w_sum-nums[i-1]+nums[i+k-1]
            max_sum=max(max_sum,w_sum)
        return max_sum/k