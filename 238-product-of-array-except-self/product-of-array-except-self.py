class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]*nums[i])
        suffix=[nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            suffix.append(suffix[-1]*nums[i])
        suffix=suffix[::-1]
        ans=[suffix[1]]
        for i in range(1,len(nums)-1):
            ans.append(prefix[i-1]*suffix[i+1])
        ans.append(prefix[-2])
        return ans