class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_size=0
        size=0
        zeros=[]
        for i in range(len(nums)):
            if nums[i]==0:
                if k==0:
                    size=0
                elif len(zeros)==k:
                    ind=zeros.pop(0)
                    zeros.append(i)
                    size=i-ind
                else:
                    size+=1
                    zeros.append(i)
                    max_size=max(size,max_size)
            else:
                size+=1
                max_size=max(size,max_size)
        return max_size
            