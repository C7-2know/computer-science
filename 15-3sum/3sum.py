class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    res.append((nums[i],nums[l],nums[r]))
                    
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return list(set(res))
                