class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backtrack(nums,arr,indx):
            if arr not in ans:
                ans.append(arr[:])
            for i in range(indx,len(nums)):
                arr.append(nums[i])
                # while i+1<len(nums) and nums[i]==nums[i+1]:
                #     i+=1
                backtrack(nums,arr,i+1)
                arr.pop()
        backtrack(nums,[],0)
        return ans