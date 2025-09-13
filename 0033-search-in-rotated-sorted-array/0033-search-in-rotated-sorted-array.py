class Solution:
    def search(self, nums: List[int], target: int) -> int:
        piv=len(nums)//2
        l,r=0,len(nums)-1

        while l<r:
            if nums[piv]>nums[r]:
                l=piv+1
                piv=l+(r-l)//2
            else:
                r=piv
                piv=(l+r)//2
        print(piv)

        if target>nums[-1]:
            l,r=0,piv
        else:
            l,r=piv,len(nums)-1
        i=(l+r)//2
        while l<r:
            if nums[i]<target:
                l=i+1
            else:
                r=i
            i=(l+r)//2
        return i if target==nums[i] else -1