class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pref=[nums[0]]
        for i in range(1,len(nums)):
            pref.append(pref[i-1]+nums[i])
        tot=pref[0]
        for i in range(1, len(pref)):
            start=max(0,i-nums[i])
            res=pref[i]
            if start!=0:
                res-=pref[start-1]
            tot+=res
        return tot