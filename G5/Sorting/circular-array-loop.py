class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        max_sz=0
        cycle=False
        for i in range(len(nums)):
            size=set([i])
            nex=(i+nums[i])%len(nums)
            # (max_sz>1 or max_sz==len(nums)-1 and cycle==True)
            for j in range(len(nums)):
                if (nums[nex]<0 and nums[i]>0) or (nums[nex]>0 and nums[i]<0):
                    break
                if nex==i:
                    # print(size)
                    if len(size)>1:
                        cycle=True
                    max_sz=max(max_sz,len(size))
                    break
                size.add(nex)
                nex=(nex+nums[nex])%len(nums)
        # print(max_sz)
        return cycle