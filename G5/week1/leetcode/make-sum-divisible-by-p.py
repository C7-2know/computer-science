class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dc={0:-1}
        total=sum(nums)
        if total<p:
            return -1
        if total%p==0:
            return 0
        count=float('inf')
        rem=total%p
        r_sum=0
        for i in range(len(nums)):
            r_sum+=nums[i]
            c_rem=r_sum%p
            if (c_rem-rem+p)%p in dc and i-dc[(c_rem-rem+p)%p]!=len(nums):
                count=min(count,i-dc[(c_rem-rem+p)%p])   
            dc[c_rem%p]=i
            # print(dc)
        if count==float('inf'):
            count=-1
        return count      