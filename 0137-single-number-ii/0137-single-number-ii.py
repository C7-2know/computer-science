class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        print(bin(~2))
        print(bin(~1),bin(1))
        nums.sort()
        i=0
        while i <len(nums)-1:
            print(nums[i])
            if nums[i]==nums[i+1]:
                i+=3
            else:
                return nums[i]
        
        return nums[i]
        # return 2