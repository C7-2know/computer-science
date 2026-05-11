class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        tot=0
        if len(nums)<3:
            return 0
        i,j=0,2
        d=nums[1]-nums[0]
        while j<len(nums):
            if nums[j]-nums[j-1]!=d:
                i+=1
                while j-1-i>1:
                    tot+=(j-1-i-1)
                    i+=1
                i=j-1
                d=nums[j]-nums[i]
            else:
                if j-i>1:
                    tot+=1
            j+=1
        j-=1
        i+=1
        while j-i>=2:
            tot+=(j-i-1)
            i+=1
        return tot
            