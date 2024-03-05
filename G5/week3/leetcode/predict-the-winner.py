class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(nums,l,r,p):
            # if l==r:
            #     return nums[l]
            if l>r:
                return 0
            if p==1:
                left=nums[l]+backtrack(nums,l+1,r,0)
                right=nums[r]+backtrack(nums,l,r-1,0)
                return max(left,right)

            if p==0:
                left=backtrack(nums,l+1,r,1)
                right=backtrack(nums,l,r-1,1)
                return min(left,right)
        p1=backtrack(nums,0,len(nums)-1,1)
        return p1>=sum(nums)-p1