class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        total=0
        dc={0:1}
        for i in range(len(nums)):
            total+=nums[i]
            nums[i]=total
            if nums[i]-goal in dc:
                count+=dc[nums[i]-goal]
            dc[total]=dc.get(total,0)+1
        return count
