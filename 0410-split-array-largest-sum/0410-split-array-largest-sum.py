class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        max_=sum(nums)
        min_=min(nums)
        def is_pos(sum_,k):
            count=1
            cur=0
            for i in range(len(nums)):
                if nums[i]>sum_:
                    return False
                if cur+nums[i]>sum_:
                    count+=1
                    cur=0
                cur+=nums[i]
            return count<=k
        ans=float('inf')
        while max_>=min_:
            mid=(max_+min_)//2
            if is_pos(mid,k):
                max_=mid-1
                ans=min(ans,mid)
            else:
                min_=mid+1
        return ans
