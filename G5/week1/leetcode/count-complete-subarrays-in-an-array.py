class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        arr=set(nums)
        w_dc={}
        n=0
        left=0
        comp=0
        for i in range(len(nums)):
            if nums[i] not in w_dc:
                n+=1
                w_dc[nums[i]]=0
            w_dc[nums[i]]+=1
            while n==len(arr):
                comp+=len(nums)-i
                w_dc[nums[left]]-=1
                if w_dc[nums[left]]==0:
                    n-=1
                    w_dc.pop(nums[left])
                left+=1
        return comp