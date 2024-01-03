class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first=0
        sec=1
        while sec<len(nums):
            if nums[first]==nums[sec]:
                nums[sec]='_'
                sec+=1
            else:
                nums[first+1],nums[sec]=nums[sec],nums[first+1]
                first+=1
                sec+=1
        # print(nums)
        # print(first,sec)
        return first+1