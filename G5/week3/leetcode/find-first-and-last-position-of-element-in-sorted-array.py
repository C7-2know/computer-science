class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st=-1
        for i in range(len(nums)):
            if nums[i]==target and st==-1:
                st=i
            elif st!=-1 and nums[i]!=target:
                return [st,i-1]
        if nums and nums[-1]==target:
            return [st,len(nums)-1]
        else:
            return [-1,-1]