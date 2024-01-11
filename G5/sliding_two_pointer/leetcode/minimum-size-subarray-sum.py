class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_num=float('inf')
        ls=0
        st=0
        wind=0
        while ls<len(nums):
            if wind>=target:
                min_num=min(min_num,ls-st)
                wind-=nums[st]
                st+=1
            else:
                wind+=nums[ls]
                ls+=1
        while wind>=target:
            wind-=nums[st]
            min_num=min(min_num,ls-st)
            st+=1
        return 0 if min_num==float('inf') else min_num