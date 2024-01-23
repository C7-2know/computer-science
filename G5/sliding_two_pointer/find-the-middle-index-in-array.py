class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        indx=-1
        for j in range(len(nums)):
            if j==0:
                left=0
            else:
                left=nums[j-1]
            if nums[-1]-nums[j]==left:
                indx=j
                break
        return indx