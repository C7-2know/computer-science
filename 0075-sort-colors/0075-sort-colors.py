class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors=[0,1,2]
        p1,p2=0,0
        for c in colors[:-1]:
            while p2<len(nums):
                while p1<len(nums) and nums[p1]==c:
                    p1+=1
                if p2<p1:
                    if p1>=len(nums):
                        break
                    p2=p1
                if nums[p2]==c:
                    nums[p1], nums[p2]=nums[p2], nums[p1]
                    p1+=1
                p2+=1
            p2=p1