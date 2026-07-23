class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dc={}
        sum_=0
        max_=0
        for i in range(len(nums)):
            sum_+=nums[i]
            mod=sum_%k
            if (mod==0 and i>0) or (mod in dc and i-dc[mod]>1):
                return True
            if mod not in dc:
                dc[mod]=i
            
        return False
