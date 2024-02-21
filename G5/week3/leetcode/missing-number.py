class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ=sum(nums)
        n=len(nums)+1
        main_sum=n*(n-1)/2
        return int(main_sum-summ)