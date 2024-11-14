class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        count=0
        nums.sort()
        l,r=len(nums)-1,len(nums)-1
        for i in range(len(nums)-1):
            move=False
            while l>i and nums[i]+nums[l]>=lower:
                l-=1
                move=True
            
            if move or l<=i:
                l=min(l+1,len(nums)-1)

            while r>=l and nums[r]+nums[i]>upper:
                r-=1
            
            if r>=l and nums[i]+nums[l]>=lower and  nums[r]+nums[i]<=upper:
                count+=(r-l+1)
        return count