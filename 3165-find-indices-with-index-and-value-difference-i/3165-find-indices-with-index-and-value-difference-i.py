class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        k=indexDifference
        for i in range(len(nums)-k):
            for j in range(i+k,len(nums)):
                if abs(nums[i]-nums[j])>=valueDifference:
                    return [i,j]
        return [-1,-1]