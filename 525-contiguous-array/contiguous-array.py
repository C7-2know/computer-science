class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dc={}
        sum_=0
        max_=0
        for i in range(len(nums)):
            if nums[i]:
                sum_+=1
            else:
                sum_-=1
            if sum_ not in dc:
                dc[sum_]=i
            max_=max(max_, i-dc[sum_])
            if sum_==0:
                max_= i+1
        return max_