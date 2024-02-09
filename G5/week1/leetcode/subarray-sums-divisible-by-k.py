class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        total=0
        dc={0:1}
        for i in range(len(nums)):
            total+=nums[i]
            nums[i]=total
            rem=nums[i]%k
            if rem in dc:
                count+=dc[rem]
            dc[rem]=dc.get(rem,0)+1
        return count