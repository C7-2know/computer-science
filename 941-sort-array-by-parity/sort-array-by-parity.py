class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        od,ev=len(nums)-1,0
        while ev<od:
            while ev<len(nums) and nums[ev]%2==0:
                ev+=1
            while od>=0 and nums[od]%2!=0:
                od-=1
            if ev>od:
                return nums
            nums[ev],nums[od]=nums[od],nums[ev]
            od-=1
            ev+=1
        return nums