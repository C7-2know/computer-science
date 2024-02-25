class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(2,len(nums)):
            left=0
            right=i-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    count+=right-left
                    right-=1
                else:
                    left+=1
        return count
