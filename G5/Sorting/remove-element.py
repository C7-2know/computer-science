class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first=0
        last=len(nums)-1
        while first<=last:
            while nums[last]==val:
                nums[last]='_'
                if last==first:
                    return last
                last-=1
            if nums[first]==val:
                # nums[first]='_'
                nums[first],nums[last]=nums[last],nums[first]
                nums[last]='_'
                last-=1
            first+=1
        return first
            