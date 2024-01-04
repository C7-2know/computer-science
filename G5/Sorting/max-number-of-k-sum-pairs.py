class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        opr=0
        while left<right:
            added=nums[left]+nums[right]
            if added==k:
                opr+=1
                left+=1
                right-=1
            elif added>k:
                right-=1
            else:
                left+=1
        return opr
