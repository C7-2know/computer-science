class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # max_=max(nums)
        # return nums.index(max_)
        def is_peak(ind):
            if len(nums)==1:
                return True
            if ind==0:
                return nums[ind]>nums[ind+1]
            elif ind==len(nums)-1:
                return nums[ind]>nums[ind-1]
            return nums[ind]>nums[ind-1] and nums[ind]>nums[ind+1]
        l,r=0,len(nums)-1
        while l<=r:
            md=(l+r)//2
            if is_peak(md):
                return md
            elif nums[md]<nums[md+1]:
                l=md+1
            else:
                r=md-1
        return r

