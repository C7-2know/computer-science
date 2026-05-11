class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod=1
        i=0
        count=0
        for j in range(len(nums)):
            prod*=nums[j]
            if prod>=k:
                while i<j and prod>=k:
                    if prod/nums[j]<k:
                        count+=(j-i)
                    prod/=nums[i]
                    i+=1          
        while i<=j and prod<k:
            count+=(j-i+1)
            i+=1
        return count
