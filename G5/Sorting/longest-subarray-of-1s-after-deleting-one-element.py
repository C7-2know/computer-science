class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        delete=False
        del_ind=0
        max_size=0
        size=0
        for i in range(len(nums)):
            if nums[i]==0:
                if not delete:
                    delete=True
                    del_ind=i
                else:
                    size=i-del_ind-1
                    del_ind=i
            else:
                size+=1
                max_size=max(size,max_size)
        if not delete:
            return max_size-1
        return max_size
                