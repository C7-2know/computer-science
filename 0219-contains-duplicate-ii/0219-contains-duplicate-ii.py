class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dc={}
        for i in range(len(nums)):
            if nums[i] in dc:
                ls=dc[nums[i]]
                if i-ls<=k:
                    return True
            dc[nums[i]]=i
        return False
            